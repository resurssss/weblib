<template>
  <section>
    <h1>Каталог книг</h1>

    <label>
      Фильтр по доступности:
      <select v-model="filterAvailable" @change="fetchBooks">
        <option value="">Все</option>
        <option value="true">Доступные</option>
        <option value="false">Недоступные</option>
      </select>
    </label>

    <label>
      Сортировка:
      <select v-model="sortBy" @change="fetchBooks">
        <option value="date">По дате</option>
        <option value="title">По названию</option>
      </select>
    </label>

    <BookList
      :books="books"
      @edit="editBook"
      @delete="deleteBook"
      @toggle-status="toggleStatus"
      @toggle-favorite="toggleFavorite"
      @toggle-reserve="toggleReserve"
    />
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import BookList from '../components/BookList.vue'
import api from '../services/api'

const books = ref([])
const filterAvailable = ref('')
const sortBy = ref('date')

function fetchBooks() {
  let params = {}
  if (filterAvailable.value !== '') params.available = filterAvailable.value
  if (sortBy.value) params.sort = sortBy.value

  api.get('/books', { params })
    .then(res => { books.value = res.data })
    .catch(err => console.error(err))
}

function editBook(id) {
  console.log('edit', id)
}

function deleteBook(id) {
  api.delete(`/books/${id}`)
    .then(() => fetchBooks())
}

function toggleStatus(id) {
  api.patch(`/books/${id}/status`)
    .then(() => fetchBooks())
}

function toggleFavorite(id) {
  api.patch(`/books/${id}/favorite`)
    .then(() => fetchBooks())
}

function toggleReserve(id) {
  api.patch(`/books/${id}/reserve`)
    .then(() => fetchBooks())
}

onMounted(fetchBooks)
</script>