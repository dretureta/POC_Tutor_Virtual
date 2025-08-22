<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h3 class="text-lg font-medium text-gray-700 mb-4">Importar Estudiantes desde CSV</h3>
    <p class="text-sm text-gray-600 mb-4">
      Sube un archivo CSV con las columnas: `first_name`, `last_name`, `school`.
    </p>

    <div class="flex items-center space-x-4">
      <input
        type="file"
        @change="handleFileSelect"
        accept=".csv"
        class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
      />
      <button
        @click="handleUpload"
        :disabled="!selectedFile || adminStore.uploading"
        class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400"
      >
        <span v-if="adminStore.uploading">Subiendo...</span>
        <span v-else>Subir</span>
      </button>
    </div>

    <div v-if="adminStore.uploadSuccessMessage" class="mt-4 text-sm text-green-600">
      {{ adminStore.uploadSuccessMessage }}
    </div>
    <div v-if="adminStore.uploadError" class="mt-4 text-sm text-red-600">
      {{ adminStore.uploadError }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAdminStore } from '~/stores/adminStore'

const adminStore = useAdminStore()
const selectedFile = ref<File | null>(null)

const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    selectedFile.value = target.files[0]
  }
}

const handleUpload = () => {
  if (selectedFile.value) {
    adminStore.uploadStudentsCSV(selectedFile.value)
  }
}
</script>
