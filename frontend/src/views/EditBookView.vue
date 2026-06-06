<template>
  <section>
    <h1>Редактирование книги</h1>

    <p v-if="loading">Загрузка...</p>

    <BookForm
      v-else
      :initial-book="book"
      submit-text="Сохранить изменения"
      @submit="updateBook"
    />
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
  const response = await api.get(`/books/${route.params.id}`)
  book.value = response.data
  loading.value = false
}

async function updateBook(formData) {
  await api.put(`/books/${route.params.id}`, formData)
  router.push({ name: 'books' })
}

onMounted(fetchBook)
</script>