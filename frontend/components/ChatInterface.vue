<template>
  <div class="flex flex-col h-[60vh] bg-white rounded-lg shadow-md">
    <!-- Header -->
    <div class="p-4 border-b">
      <h3 class="text-xl font-semibold text-gray-700">Chat con Tutor de {{ tutorType }}</h3>
    </div>

    <!-- Message Display -->
    <div class="flex-1 p-4 space-y-4 overflow-y-auto" aria-live="polite" aria-atomic="true">
      <div v-if="chatStore.loading">Cargando historial...</div>
      <div v-else-if="chatStore.error" class="text-red-500">{{ chatStore.error }}</div>
      <div v-else-if="!chatStore.conversation || chatStore.conversation.messages.length === 0" class="text-gray-500 text-center">
        No hay mensajes. ¡Comienza la conversación!
      </div>
      <div v-else v-for="(msg, index) in chatStore.conversation.messages" :key="index" class="flex" :class="msg.role === 'user' ? 'justify-end' : 'justify-start'">
        <div class="max-w-md px-4 py-2 rounded-lg" :class="msg.role === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-800'">
          <p>{{ msg.content }}</p>
        </div>
      </div>
    </div>

    <!-- Message Input -->
    <div class="p-4 border-t">
      <div class="flex items-center">
        <label for="chat-input" class="sr-only">Mensaje</label>
        <input
          id="chat-input"
          v-model="newMessage"
          @keyup.enter="handleSend"
          type="text"
          placeholder="Escribe tu mensaje..."
          class="flex-1 px-4 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          :disabled="isSending"
        />
        <button
          @click="handleSend"
          aria-label="Enviar mensaje"
          class="ml-4 px-6 py-2 bg-blue-500 text-white rounded-full hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-blue-300"
          :disabled="isSending || !newMessage.trim()"
        >
          Enviar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useChatStore } from '~/stores/chatStore'

const props = defineProps({
  studentId: {
    type: String,
    required: true
  },
  tutorType: {
    type: String,
    default: 'Matemáticas'
  }
})

const chatStore = useChatStore()
const newMessage = ref('')
const isSending = ref(false)

onMounted(() => {
  chatStore.fetchConversation(props.studentId, props.tutorType)
})

const handleSend = async () => {
  if (!newMessage.value.trim()) return

  isSending.value = true
  const messageToSend = newMessage.value
  newMessage.value = ''

  // For this POC, the sendMessage action is simulated and doesn't represent a real API call flow for n8n webhooks.
  // In a real scenario, this would likely hit a backend endpoint that then triggers the n8n webhook.
  // The store currently has a placeholder for this logic.
  await chatStore.sendMessage(props.studentId, props.tutorType, messageToSend)

  isSending.value = false
}
</script>
