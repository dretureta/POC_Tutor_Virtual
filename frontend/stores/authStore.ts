import { defineStore } from 'pinia'

interface User {
  id: string;
  email: string;
  is_active: boolean;
}

export const useAuthStore = defineStore('authStore', {
  state: () => ({
    token: useCookie('auth_token').value || null as string | null,
    user: null as User | null,
    loading: false,
    error: null as string | null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
  },

  actions: {
    async login(credentials: { username: string; password: string }) {
      this.loading = true
      this.error = null
      const config = useRuntimeConfig()

      try {
        const response = await $fetch<{ access_token: string }>(`${config.public.apiBase}/auth/token`, {
          method: 'POST',
          body: new URLSearchParams(credentials),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })

        const token = response.access_token
        this.token = token
        const tokenCookie = useCookie('auth_token')
        tokenCookie.value = token

        await this.fetchUserProfile()

        return true
      } catch (e: any) {
        this.error = e.data?.detail || 'Error al iniciar sesión.'
        return false
      } finally {
        this.loading = false
      }
    },

    logout() {
      const tokenCookie = useCookie('auth_token')
      tokenCookie.value = null
      this.token = null
      this.user = null
      // Redirect to login page
      const router = useRouter()
      router.push('/login')
    },

    async fetchUserProfile() {
      if (!this.token) return

      const { $api } = useNuxtApp()
      try {
        const user = await $api<User>('/auth/me')
        this.user = user
      } catch (e) {
        console.error("Failed to fetch user profile", e)
        this.logout() // Log out if token is invalid
      }
    }
  },
})
