<template>
  <section class="create-book-page">
    <div class="create-container">
      <h4 class="c-title">Создать книгу</h4>

      <div class="form-wrapper">
        <BookForm
          submit-text="Создать книгу"
          @submit="createBook"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
import BookForm from '../components/BookForm.vue'
import api from '../services/api'

const router = useRouter()

async function createBook(formData) {
  try {
    await api.post('/books', formData)
    router.push({ name: 'books' })
  } catch (error) {
    console.error('Ошибка при создании книги:', error)
    alert('Ошибка при создании книги')
  }
}
</script>

<style scoped>
.create-book-page {
  min-height: 100vh;
  padding: 2rem;
}

.create-container {
  max-width: 1100px;
  margin: 0 auto;
  width: 100%;
}

.c-title {
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

@media (max-width: 768px) {
  .create-book-page {
    padding: 1rem;
  }
  
  .c-title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .form-wrapper {
    border-radius: 16px;
  }
}
</style>