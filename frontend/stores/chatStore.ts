import { defineStore } from 'pinia'

interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
}

interface Conversation {
  id: string;
  tutor_type: string;
  messages: Message[];
}

export const useChatStore = defineStore('chatStore', {
  state: () => ({
    conversation: null as Conversation | null,
    loading: false,
    error: null as string | null,
  }),

  actions: {
    async fetchConversation(studentId: string, tutorType: string) {
      this.loading = true
      this.error = null
      const config = useRuntimeConfig()

      try {
        // This endpoint returns a list of conversations, we'll find the right one
        const conversations = await $fetch<Conversation[]>(`${config.public.apiBase}/conversations/${studentId}`)
        this.conversation = conversations.find(c => c.tutor_type === tutorType) || null
      } catch (e: any) {
        // If not found (404), it's not an error, just no history.
        if (e.response?.status !== 404) {
          this.error = e.message
        }
        this.conversation = null
      } finally {
        this.loading = false
      }
    },

    async sendMessage(studentId: string, tutorType: string, message: string) {
        const userMessage: Message = { role: 'user', content: message };
        if (!this.conversation || this.conversation.tutor_type !== tutorType) {
            this.conversation = { id: '', tutor_type: tutorType, messages: [userMessage] };
        } else {
            this.conversation.messages.push(userMessage);
        }

        const webhookPath = tutorType === 'Matemáticas' ? '/tutor-math' : '/tutor-language';

        try {
            // NOTE: In a real app, this would be a call to the n8n webhook URL,
            // which is on a different port. This is a placeholder.
            const response = await $fetch<string>(`/api${webhookPath}`, {
                method: 'POST',
                body: { student_id: studentId, message: message }
            });

            const assistantMessage: Message = { role: 'assistant', content: response };
            this.conversation.messages.push(assistantMessage);

        } catch (e: any) {
            this.error = `Error al conectar con el tutor de ${tutorType}: ${e.message}`;
            this.conversation.messages.pop();
        }
    },
  },
})
