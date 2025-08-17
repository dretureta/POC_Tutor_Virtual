import { useAuthStore } from '~/stores/authStore'

export default defineNuxtRouteMiddleware((to, from) => {
  const authStore = useAuthStore()

  // If the user is not authenticated and trying to access a protected route
  if (!authStore.isAuthenticated && to.path !== '/login') {
    // Redirect them to the login page
    return navigateTo('/login')
  }

  // If the user is authenticated and trying to access the login page
  if (authStore.isAuthenticated && to.path === '/login') {
    // Redirect them to the home page
    return navigateTo('/')
  }
})
