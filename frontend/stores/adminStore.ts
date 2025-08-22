import { defineStore } from 'pinia'

export const useAdminStore = defineStore('adminStore', {
  state: () => ({
    uploading: false,
    uploadError: null as string | null,
    uploadSuccessMessage: null as string | null,
  }),

  actions: {
    async uploadStudentsCSV(file: File) {
      this.uploading = true
      this.uploadError = null
      this.uploadSuccessMessage = null

      const { $api } = useNuxtApp()
      const formData = new FormData()
      formData.append('file', file)

      try {
        const response = await $api<{ message: string }>('/students/upload-csv', {
          method: 'POST',
          body: formData,
        })
        this.uploadSuccessMessage = response.message
      } catch (e: any) {
        this.uploadError = e.data?.detail || 'Error al subir el archivo.'
      } finally {
        this.uploading = false
      }
    },
  },
})
