<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Sidebar -->
    <aside class="w-64 flex-shrink-0 bg-gray-800 text-white">
      <div class="p-4 text-2xl font-bold">
        Tutor Virtual
      </div>
      <nav class="mt-5">
        <ul>
          <li>
            <a href="#" class="block px-4 py-2 mt-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-white">
              Dashboard
            </a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 mt-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-white">
              Estudiantes
            </a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 mt-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-white">
              Alertas
            </a>
          </li>
        </ul>
      </nav>
    </aside>

    <!-- Main content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <!-- Header -->
      <header class="flex justify-between items-center p-4 bg-white border-b">
        <h1 class="text-xl font-semibold">Dashboard Principal</h1>
        <div>
          <!-- Placeholder for user menu or actions -->
          <span class="text-gray-600">Usuario Admin</span>
        </div>
      </header>

      <!-- Page Content -->
      <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100 p-4">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
// Layout script setup if needed
</script>

<style scoped>
/* Scoped styles for the layout if needed */
</style>
