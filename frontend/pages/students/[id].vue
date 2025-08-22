<template>
  <div>
    <!-- Loading State -->
    <div v-if="studentStore.loading && !student" class="text-center">
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
          <div class="flex items-center space-x-4">
            <div class="text-right">
              <p class="text-2xl font-bold text-blue-600">{{ student.points }}</p>
              <p class="text-sm text-gray-500">Puntos</p>
            </div>
            <RiskBadge :risk-level="student.risk_level" />
          </div>
        </div>
      </div>

      <!-- Gamification Section -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-xl font-semibold text-gray-700 mb-4">Logros y Recompensas</h3>
        <div v-if="student.badges && student.badges.length > 0" class="flex flex-wrap gap-4">
          <Badge v-for="studentBadge in student.badges" :key="studentBadge.badge.id" :badge="studentBadge.badge" />
        </div>
        <div v-else class="text-gray-500">
          Este estudiante aún no ha ganado insignias.
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

      <!-- Chat Section -->
      <div>
        <div class="mb-4 border-b border-gray-200">
            <nav class="-mb-px flex space-x-8" aria-label="Tabs">
                <button
                    v-for="tutor in tutors"
                    :key="tutor.name"
                    @click="selectedTutor = tutor.name"
                    :class="[
                        tutor.name === selectedTutor
                            ? 'border-blue-500 text-blue-600'
                            : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
                        'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm'
                    ]"
                >
                    Tutor de {{ tutor.name }}
                </button>
            </nav>
        </div>

        <LazyChatInterface :student-id="student.id" :tutor-type="selectedTutor" :key="selectedTutor" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useStudentStore } from '~/stores/studentStore'
import { computed, ref } from 'vue'
import RiskBadge from '~/components/RiskBadge.vue'
import EvaluationCard from '~/components/EvaluationCard.vue'
import Badge from '~/components/Badge.vue'

definePageMeta({
  layout: 'default'
})

const route = useRoute()
const studentStore = useStudentStore()
const studentId = route.params.id as string

const tutors = [
  { name: 'Matemáticas', webhook: '/tutor-math' },
  { name: 'Lengua', webhook: '/tutor-language' },
]
const selectedTutor = ref(tutors[0].name)

studentStore.fetchStudentById(studentId)

const student = computed(() => studentStore.selectedStudent)
</script>
