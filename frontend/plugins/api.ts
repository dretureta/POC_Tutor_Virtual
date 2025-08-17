import { ofetch } from 'ofetch'
import { useAuthStore } from '~/stores/authStore'

export default defineNuxtPlugin((_nuxtApp) => {
  const config = useRuntimeConfig()
  const authStore = useAuthStore()

  const api = ofetch.create({
    baseURL: config.public.apiBase,
    onRequest({ request, options }) {
      if (authStore.token) {
        options.headers = new Headers(options.headers)
        options.headers.set('Authorization', `Bearer ${authStore.token}`)
      }
    },
    onResponseError({ response }) {
      if (response.status === 401) {
        authStore.logout()
        navigateTo('/login')
      }
    }
  })

  // Expose the api client to the whole app
  return {
    provide: {
      api
    }
  }
})
