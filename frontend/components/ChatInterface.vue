<template>
  <div class="flex flex-col h-[60vh] bg-white rounded-lg shadow-md">
    <!-- Header -->
    <div class="p-4 border-b flex justify-between items-center">
      <h3 class="text-xl font-semibold text-gray-700">Chat con Tutor de {{ tutorType }}</h3>
      <div class="w-4 h-4 rounded-full" :class="chatStore.isConnected ? 'bg-green-500' : 'bg-red-500'"></div>
    </div>

    <!-- Message Display -->
    <div ref="messageContainer" class="flex-1 p-4 space-y-4 overflow-y-auto" aria-live="polite" aria-atomic="true">
      <div v-if="chatStore.loading">Cargando historial...</div>
      <div v-else-if="chatStore.error" class="text-red-500">{{ chatStore.error }}</div>
      <div v-else-if="!chatStore.messages || chatStore.messages.length === 0" class="text-gray-500 text-center">
        No hay mensajes. ¡Comienza la conversación!
      </div>
      <div v-else v-for="(msg, index) in chatStore.messages" :key="index" class="flex" :class="msg.role === 'user' ? 'justify-end' : 'justify-start'">
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
          :disabled="!chatStore.isConnected"
        />
        <button
          @click="handleSend"
          aria-label="Enviar mensaje"
          class="ml-4 px-6 py-2 bg-blue-500 text-white rounded-full hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-400"
          :disabled="!chatStore.isConnected || !newMessage.trim()"
        >
          Enviar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useChatStore } from '~/stores/chatStore'
import { storeToRefs } from 'pinia';

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
const { messages } = storeToRefs(chatStore)
const newMessage = ref('')
const messageContainer = ref<HTMLDivElement | null>(null)

// Scroll to bottom when new messages are added
watch(messages, async () => {
  await nextTick()
  if (messageContainer.value) {
    messageContainer.value.scrollTop = messageContainer.value.scrollHeight
  }
}, { deep: true })

onMounted(async () => {
  // Fetch initial history via HTTP
  await chatStore.fetchHistory(props.studentId, props.tutorType)
  // Connect to WebSocket for real-time messages
  chatStore.connect(props.studentId, props.tutorType)
})

onUnmounted(() => {
  chatStore.disconnect()
})

const handleSend = () => {
  if (!newMessage.value.trim()) return
  chatStore.sendMessage(newMessage.value)
  newMessage.value = ''
}
</script>
