import { defineStore } from 'pinia'

// Define the type for a student object
interface Student {
  id: string;
  first_name: string;
  last_name: string;
  school: string;
  risk_level: 'low' | 'medium' | 'high';
  // Add other properties as needed
}

// Add Evaluation type
interface Evaluation {
  id: string;
  subject: { name: string };
  score: number;
  date: string;
}

// Update Student type to include evaluations
interface Student {
  id: string;
  first_name: string;
  last_name: string;
  school: string;
  risk_level: 'low' | 'medium' | 'high';
  evaluations: Evaluation[];
}

export const useStudentStore = defineStore('studentStore', {
  state: () => ({
    students: [] as Student[],
    selectedStudent: null as Student | null,
    loading: false,
    error: null as string | null,
  }),

  getters: {
    allStudents: (state) => state.students,
    studentCount: (state) => state.students.length,
    atRiskStudents: (state) => state.students.filter(s => s.risk_level !== 'low'),
  },

  actions: {
    async fetchStudents() {
      this.loading = true
      this.error = null
      const { $api } = useNuxtApp()
      try {
        const data = await $api<Student[]>('/students')
        this.students = data
      } catch (e: any) {
        this.error = e.data?.detail || 'Failed to fetch students'
      } finally {
        this.loading = false
      }
    },
    async fetchStudentById(id: string) {
      this.loading = true
      this.error = null
      this.selectedStudent = null
      const { $api } = useNuxtApp()
      try {
        const data = await $api<Student>(`/students/${id}`)
        this.selectedStudent = data
      } catch (e: any) {
        this.error = e.data?.detail || 'Failed to fetch student'
      } finally {
        this.loading = false
      }
    },
  },
})
