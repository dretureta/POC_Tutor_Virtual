import { defineStore } from 'pinia'
import { useAuthStore } from './authStore'

interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
}

export const useChatStore = defineStore('chatStore', {
  state: () => ({
    messages: [] as Message[],
    socket: null as WebSocket | null,
    isConnected: false,
    loading: false,
    error: null as string | null,
  }),

  actions: {
    async fetchHistory(studentId: string, tutorType: string) {
      // This part remains the same, to load initial history
      this.loading = true
      this.error = null
      const { $api } = useNuxtApp()
      try {
        const conversations = await $api<any[]>(`/conversations/${studentId}`)
        const relevantConversation = conversations.find(c => c.tutor_type === tutorType)
        this.messages = relevantConversation ? relevantConversation.messages : []
      } catch (e: any) {
        if (e.response?.status !== 404) {
          this.error = "No se pudo cargar el historial de chat."
        }
        this.messages = []
      } finally {
        this.loading = false
      }
    },

    connect(studentId: string, tutorType: string) {
      if (this.socket || this.isConnected) {
        this.disconnect()
      }

      const authStore = useAuthStore()
      if (!authStore.token) {
        this.error = "No estás autenticado."
        return
      }

      // Use wss for secure connections in production
      const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
      // Use the main host, not the API port
      const wsUrl = `${wsProtocol}//${window.location.host}/api/chat/ws/chat/${studentId}/${tutorType}?token=${authStore.token}`

      console.log(`Connecting to WebSocket: ${wsUrl}`)
      this.socket = new WebSocket(wsUrl)

      this.socket.onopen = () => {
        console.log("WebSocket connection established.")
        this.isConnected = true
        this.error = null
      }

      this.socket.onmessage = (event) => {
        const message: Message = { role: 'assistant', content: event.data }
        this.messages.push(message)
      }

      this.socket.onerror = (event) => {
        console.error("WebSocket error:", event)
        this.error = "Error en la conexión del chat en tiempo real."
        this.isConnected = false
      }

      this.socket.onclose = () => {
        console.log("WebSocket connection closed.")
        this.isConnected = false
        this.socket = null
      }
    },

    disconnect() {
      if (this.socket) {
        this.socket.close()
      }
    },

    sendMessage(message: string) {
      if (this.socket && this.isConnected) {
        const userMessage: Message = { role: 'user', content: message }
        this.messages.push(userMessage)
        this.socket.send(message)
      } else {
        this.error = "No hay una conexión activa para enviar el mensaje."
      }
    },
  },
})
