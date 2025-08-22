<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/authStore'

const authStore = useAuthStore()

// If a token exists on app load, fetch the user profile
if (authStore.isAuthenticated) {
  authStore.fetchUserProfile()
}
</script>

<style>
body {
  font-family: 'sans-serif';
  background-color: #f4f4f5; /* zinc-100 from tailwind */
}
</style>
