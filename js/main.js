import { initScrollAnimations } from './scroll-animations.js'
import { initMarquee } from './marquee.js'
import { initMobileNav } from './mobile-nav.js'

function updateFooterYear() {
  const el = document.getElementById('footer-year')
  if (el) el.textContent = new Date().getFullYear()
}

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations()
  initMarquee()
  initMobileNav()
  updateFooterYear()
})
