<template>
  <div>
    <!-- Loading State -->
    <div v-if="studentStore.loading" class="text-center">
      Cargando datos del estudiante...
    </div>

    <!-- Error State -->
    <div v-else-if="studentStore.error" class="text-red-500 text-center">
      Error: {{ studentStore.error }}
    </div>

    <!-- Student Data -->
    <div v-else-if="student" class="space-y-8">
      <!-- Student Header -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-3xl font-bold text-gray-800">
              {{ student.first_name }} {{ student.last_name }}
            </h2>
            <p class="text-gray-600 mt-1">{{ student.school }}</p>
          </div>
          <RiskBadge :risk-level="student.risk_level" />
        </div>
      </div>

      <!-- Evaluations List -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-xl font-semibold text-gray-700 mb-4">Historial de Evaluaciones</h3>
        <div v-if="student.evaluations && student.evaluations.length > 0" class="space-y-3">
          <EvaluationCard
            v-for="evaluation in student.evaluations"
            :key="evaluation.id"
            :evaluation="evaluation"
          />
        </div>
        <div v-else class="text-gray-500">
          No hay evaluaciones registradas para este estudiante.
        </div>
      </div>

      <!-- Chat Interface -->
      <ChatInterface :student-id="student.id" tutor-type="Matemáticas" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useStudentStore } from '~/stores/studentStore'
import { computed } from 'vue'
import RiskBadge from '~/components/RiskBadge.vue'
import EvaluationCard from '~/components/EvaluationCard.vue'
import ChatInterface from '~/components/ChatInterface.vue'

definePageMeta({
  layout: 'default'
})

const route = useRoute()
const studentStore = useStudentStore()
const studentId = route.params.id as string

// Fetch student data
await studentStore.fetchStudentById(studentId)

// Computed property to get the student from the store
const student = computed(() => studentStore.selectedStudent)
</script>
