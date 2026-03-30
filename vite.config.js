import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        career: resolve(__dirname, 'career.html'),
        press: resolve(__dirname, 'press.html'),
        contact: resolve(__dirname, 'contact.html'),
      },
    },
  },
})
