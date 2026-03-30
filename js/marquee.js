export function initMarquee() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (prefersReducedMotion) return

  document.querySelectorAll('.marquee').forEach(marquee => {
    const content = marquee.querySelector('.marquee__content')
    if (!content) return

    const clone = content.cloneNode(true)
    clone.setAttribute('aria-hidden', 'true')
    marquee.appendChild(clone)
  })
}
