import { visualizer } from 'rollup-plugin-visualizer'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  vite: {
    plugins: [
      process.env.ANALYZE && visualizer({
        open: true,
        filename: 'bundle-stats.html',
      }),
    ],
  },

  app: {
    head: {
      htmlAttrs: {
        lang: 'es'
      }
    }
  },

  modules: ['@nuxt/ui', '@pinia/nuxt'],

  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'http://localhost:8000/api'
    }
  },

  ui: {
    global: true,
    icons: ['mdi', 'simple-icons']
  }
})
