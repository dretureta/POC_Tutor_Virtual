<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-2xl font-bold text-center text-gray-700">Iniciar Sesión</h2>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label for="email" class="text-sm font-medium text-gray-700">Email</label>
          <input
            v-model="email"
            id="email"
            name="email"
            type="email"
            required
            class="w-full px-3 py-2 mt-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="tu@email.com"
          />
        </div>

        <div>
          <label for="password" class="text-sm font-medium text-gray-700">Contraseña</label>
          <input
            v-model="password"
            id="password"
            name="password"
            type="password"
            required
            class="w-full px-3 py-2 mt-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="********"
          />
        </div>

        <div v-if="error" class="text-sm text-red-600">
          {{ error }}
        </div>

        <div>
          <button
            type="submit"
            class="w-full px-4 py-2 font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-blue-400"
            :disabled="loading"
          >
            <span v-if="loading">Ingresando...</span>
            <span v-else>Ingresar</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '~/stores/authStore'
import { storeToRefs } from 'pinia'

const email = ref('')
const password = ref('')
const authStore = useAuthStore()
const { loading, error } = storeToRefs(authStore)
const router = useRouter()

const handleLogin = async () => {
  const success = await authStore.login({ username: email.value, password: password.value })
  if (success) {
    router.push('/') // Redirect to dashboard on successful login
  }
}

// Use a specific layout for the login page that doesn't have the sidebar/header
definePageMeta({
  layout: 'auth'
})
</script>
