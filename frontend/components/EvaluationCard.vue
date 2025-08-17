<template>
  <div class="bg-gray-50 p-3 rounded-md border border-gray-200 flex justify-between items-center">
    <div>
      <p class="font-semibold text-gray-700">{{ evaluation.subject.name }}</p>
      <p class="text-sm text-gray-500">
        Fecha: {{ new Date(evaluation.date).toLocaleDateString() }}
      </p>
    </div>
    <p :class="scoreClass" class="text-2xl font-bold">
      {{ evaluation.score }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  evaluation: {
    type: Object,
    required: true,
    default: () => ({
      subject: { name: 'Materia de Ejemplo' },
      date: new Date().toISOString(),
      score: 10
    })
  }
})

const scoreClass = computed(() => {
  if (props.evaluation.score >= 9) return 'text-green-600'
  if (props.evaluation.score >= 6) return 'text-blue-600'
  return 'text-red-600'
})
</script>
