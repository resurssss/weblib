<template>
  <section class="edit-book-page">
    <div class="edit-container">
      <h4 class="e-title">Редактирование книги</h4>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Загрузка...</p>
      </div>

      <div v-else class="form-wrapper">
        <BookForm
          :initial-book="book"
          submit-text="Сохранить изменения"
          @submit="updateBook"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import BookForm from '../components/BookForm.vue'
import api from '../services/api'

const route = useRoute()
const router = useRouter()

const book = ref(null)
const loading = ref(true)

async function fetchBook() {
  try {
    const response = await api.get(`/books/${route.params.id}`)
    book.value = response.data
  } catch (error) {
    console.error('Ошибка загрузки книги:', error)
    alert('Ошибка загрузки книги')
  } finally {
    loading.value = false
  }
}

async function updateBook(formData) {
  try {
    await api.put(`/books/${route.params.id}`, formData)
    router.push({ name: 'books' })
  } catch (error) {
    console.error('Ошибка обновления книги:', error)
    alert('Ошибка при сохранении изменений')
  }
}

onMounted(fetchBook)
</script>

<style scoped>
.edit-book-page {
  min-height: 100vh;
  padding: 2rem;
}

.edit-container {
  max-width: 1100px;
  margin: 0 auto;
  width: 100%;
}

.e-title {
  font-size: 2rem;
  color: #2e3d81;
  text-align: left;
  margin: 0 0 2rem 0;
  font-weight: 600;
}

.form-wrapper {
  background: white;
  border-radius: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: all 0.3s ease;
}

.form-wrapper:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.loading {
  text-align: center;
  padding: 4rem;
  background: white;
  border-radius: 24px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e2e8f0;
  border-top-color: #2e3d81;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading p {
  color: #718096;
}

@media (max-width: 768px) {
  .edit-book-page {
    padding: 1rem;
  }
  
  .e-title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .form-wrapper {
    border-radius: 16px;
  }
}
</style>