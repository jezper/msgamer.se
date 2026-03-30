import { initScrollAnimations } from './scroll-animations.js'
import { initMarquee } from './marquee.js'
import { initMobileNav } from './mobile-nav.js'

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations()
  initMarquee()
  initMobileNav()
})
