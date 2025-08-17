<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h3 class="text-lg font-medium text-gray-700 mb-4">Tendencia de Riesgo Estudiantil</h3>
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

// Mock data for the chart
const chartData = {
  labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
  datasets: [
    {
      label: 'Riesgo Alto',
      backgroundColor: '#ef4444', // red-500
      borderColor: '#ef4444',
      data: [8, 10, 12, 11, 15, 12]
    },
    {
      label: 'Riesgo Medio',
      backgroundColor: '#f59e0b', // amber-500
      borderColor: '#f59e0b',
      data: [20, 22, 25, 28, 24, 25]
    }
  ]
}

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false
}
</script>
