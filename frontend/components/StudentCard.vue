<template>
  <NuxtLink :to="`/students/${student.id}`" class="block hover:bg-gray-50 rounded-lg shadow-md" :aria-label="`Ver detalles de ${student.first_name} ${student.last_name}`">
    <div class="bg-white rounded-lg p-4 flex items-center justify-between">
      <div>
        <p class="text-lg font-semibold text-gray-800">{{ student.first_name }} {{ student.last_name }}</p>
        <p class="text-sm text-gray-600 mt-1">{{ student.school }}</p>
      </div>
      <div class="flex items-center">
        <RiskBadge :risk-level="student.risk_level" />
        <div class="ml-4 text-gray-400" aria-hidden="true">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
          </svg>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup lang="ts">
import RiskBadge from './RiskBadge.vue'

// Define the student prop
defineProps({
  student: {
    type: Object,
    required: true,
    default: () => ({
      first_name: 'Nombre',
      last_name: 'Apellido',
      school: 'Liceo de Ejemplo',
      risk_level: 'low'
    })
  }
})
</script>
