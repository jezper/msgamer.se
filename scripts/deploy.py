#!/usr/bin/env python3
"""
Deploy dist/ to Loopia via FTPS.

Reads credentials from .env.local at the project root.
Mirrors dist/ → remote document root: creates missing dirs, uploads files.
Does NOT delete remote files that are missing locally (safer; manual cleanup).

Usage:
    npm run deploy
    # or directly:
    python3 scripts/deploy.py
"""

from __future__ import annotations

import os
import sys
from ftplib import FTP_TLS, error_perm
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
ENV = ROOT / ".env.local"


def load_env() -> dict[str, str]:
    if not ENV.exists():
        sys.exit(f"missing {ENV}; create it with FTP_HOST/FTP_USER/FTP_PASS/DEPLOY_REMOTE_DIR")
    env: dict[str, str] = {}
    for line in ENV.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    for key in ("FTP_HOST", "FTP_USER", "FTP_PASS", "DEPLOY_REMOTE_DIR"):
        if key not in env:
            sys.exit(f"{ENV} is missing {key}")
    return env


def ensure_remote_dir(ftp: FTP_TLS, remote_dir: str) -> None:
    """Walk into remote_dir, creating components that don't exist."""
    parts = [p for p in remote_dir.split("/") if p]
    ftp.cwd("/")
    for part in parts:
        try:
            ftp.cwd(part)
        except error_perm:
            ftp.mkd(part)
            ftp.cwd(part)


def upload_tree(ftp: FTP_TLS, local_root: Path) -> tuple[int, int]:
    """Upload every file under local_root, mirroring directory structure."""
    files_uploaded = 0
    bytes_uploaded = 0
    base_remote = ftp.pwd()

    for local_path in sorted(local_root.rglob("*")):
        if local_path.is_dir():
            continue
        if local_path.name == ".DS_Store":
            continue

        rel = local_path.relative_to(local_root)
        rel_posix = rel.as_posix()

        # ensure parent dirs exist
        parts = rel_posix.split("/")
        ftp.cwd(base_remote)
        for part in parts[:-1]:
            try:
                ftp.cwd(part)
            except error_perm:
                ftp.mkd(part)
                ftp.cwd(part)

        size = local_path.stat().st_size
        with local_path.open("rb") as f:
            ftp.storbinary(f"STOR {parts[-1]}", f)
        files_uploaded += 1
        bytes_uploaded += size
        print(f"  ↑ {rel_posix}  ({size:,} B)")

    return files_uploaded, bytes_uploaded


def main() -> None:
    if not DIST.exists():
        sys.exit(f"missing {DIST}; run 'npm run build' first")

    env = load_env()
    print(f"→ FTPS {env['FTP_USER']}@{env['FTP_HOST']} → {env['DEPLOY_REMOTE_DIR']}")

    ftp = FTP_TLS(env["FTP_HOST"], timeout=30)
    ftp.login(env["FTP_USER"], env["FTP_PASS"])
    ftp.prot_p()  # encrypt data channel too
    ftp.set_pasv(True)

    ensure_remote_dir(ftp, env["DEPLOY_REMOTE_DIR"])

    files, total_bytes = upload_tree(ftp, DIST)
    ftp.quit()

    print(f"✓ {files} files, {total_bytes:,} bytes uploaded")


if __name__ == "__main__":
    main()
