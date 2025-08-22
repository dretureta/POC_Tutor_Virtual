<template>
  <UTooltip :text="badge.description">
    <div class="flex items-center space-x-2 bg-gray-100 p-2 rounded-full border border-gray-200">
      <span class="text-yellow-500">
        <!-- Using a generic star icon for all badges for now -->
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.196-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.783-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
        </svg>
      </span>
      <span class="font-semibold text-sm text-gray-700 pr-2">{{ badge.name }}</span>
    </div>
  </UTooltip>
</template>

<script setup lang="ts">
defineProps({
  badge: {
    type: Object,
    required: true,
    default: () => ({
      name: 'Insignia de Ejemplo',
      description: 'Esta es una descripción de prueba.',
      icon: 'star'
    })
  }
})
</script>
