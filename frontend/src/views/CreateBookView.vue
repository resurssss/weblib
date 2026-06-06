<template>
  <section class="create-book-page">
    <h1>Создание книги</h1>

    <BookForm
      submit-text="Создать книгу"
      @submit="createBook"
    />
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
import BookForm from '../components/BookForm.vue'
import api from '../services/api'

const router = useRouter()

async function createBook(formData) {
  await api.post('/books', formData)
  router.push({ name: 'books' })
}
</script>