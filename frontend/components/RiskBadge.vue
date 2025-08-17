<template>
  <span :class="badgeClass" class="px-2 py-1 text-xs font-semibold leading-tight rounded-full">
    {{ riskLevelText }}
  </span>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  riskLevel: {
    type: String,
    required: true,
    validator: (value: string) => ['low', 'medium', 'high'].includes(value)
  }
})

const riskLevelText = computed(() => {
  switch (props.riskLevel) {
    case 'low':
      return 'Bajo'
    case 'medium':
      return 'Medio'
    case 'high':
      return 'Alto'
    default:
      return 'Desconocido'
  }
})

const badgeClass = computed(() => {
  switch (props.riskLevel) {
    case 'low':
      return 'bg-green-100 text-green-800'
    case 'medium':
      return 'bg-yellow-100 text-yellow-800'
    case 'high':
      return 'bg-red-100 text-red-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
})
</script>
