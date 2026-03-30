export function initMobileNav() {
  const hamburger = document.querySelector('.nav__hamburger')
  const menu = document.querySelector('.nav__mobile-menu')

  if (!hamburger || !menu) return

  hamburger.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('nav__mobile-menu--open')
    hamburger.setAttribute('aria-expanded', String(isOpen))
  })

  menu.querySelectorAll('.nav__link').forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('nav__mobile-menu--open')
      hamburger.setAttribute('aria-expanded', 'false')
    })
  })

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('nav__mobile-menu--open')) {
      menu.classList.remove('nav__mobile-menu--open')
      hamburger.setAttribute('aria-expanded', 'false')
      hamburger.focus()
    }
  })
}
