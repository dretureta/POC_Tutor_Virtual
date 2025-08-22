<template>
  <div>
    <h2 class="text-2xl font-semibold text-gray-700">Dashboard de Estudiantes</h2>

    <!-- Stats Cards -->
    <div class="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-medium text-gray-700">Total Estudiantes</h3>
        <p class="text-3xl font-bold text-gray-900 mt-2">{{ studentStore.studentCount }}</p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-medium text-gray-700">En Riesgo</h3>
        <p class="text-3xl font-bold text-red-600 mt-2">{{ studentStore.atRiskStudents.length }}</p>
      </div>
       <!-- Add more stats cards as needed -->
    </div>

    <!-- Admin Section -->
    <div v-if="authStore.user?.role === 'admin'" class="mt-8">
      <h3 class="text-xl font-semibold text-gray-700 mb-4">Panel de Administración</h3>
      <CsvUploadForm />
    </div>

    <!-- Chart -->
    <div class="mt-8">
      <LazyRiskTrendChart />
    </div>

    <!-- Student List -->
    <div class="mt-8 bg-white p-6 rounded-lg shadow-md">
      <h3 class="text-lg font-medium text-gray-700 mb-4">Lista de Estudiantes</h3>

      <!-- Loading State -->
      <div v-if="studentStore.loading" class="text-center text-gray-500">
        Cargando estudiantes...
      </div>

      <!-- Error State -->
      <div v-else-if="studentStore.error" class="text-center text-red-500">
        Error al cargar los estudiantes: {{ studentStore.error }}
      </div>

      <!-- Data Loaded State -->
      <div v-else-if="studentStore.students.length > 0" class="space-y-4">
        <StudentCard
          v-for="student in studentStore.allStudents"
          :key="student.id"
          :student="student"
        />
      </div>

      <!-- No Data State -->
      <div v-else class="text-center text-gray-500">
        No se encontraron estudiantes.
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useStudentStore } from '~/stores/studentStore'
import { useAuthStore } from '~/stores/authStore'
import StudentCard from '~/components/StudentCard.vue'
import CsvUploadForm from '~/components/CsvUploadForm.vue'

definePageMeta({
  layout: 'default'
})

const studentStore = useStudentStore()
const authStore = useAuthStore()

// Fetch students when the component is mounted
onMounted(() => {
  studentStore.fetchStudents()
})
</script>
