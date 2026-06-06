<template>
  <section class="books-page">
    <h1>Каталог книг</h1>

    <div class="controls">
      <label>
        Фильтр по статусу:
        <select v-model="statusFilter">
          <option value="all">Все</option>
          <option value="available">В наличии</option>
        </select>
      </label>

      <label>
        Сортировка:
        <select v-model="sortType">
          <option value="date">По дате добавления</option>
          <option value="title">По алфавиту</option>
        </select>
      </label>
    </div>

    <p>Всего книг после фильтрации: {{ filteredAndSortedBooks.length }}</p>

    <p v-if="loading">Загрузка...</p>

    <p v-else-if="filteredAndSortedBooks.length === 0">
      Список книг пуст.
    </p>

    <BookList
      v-else
      :books="filteredAndSortedBooks"
      @edit="editBook"
      @delete="deleteBook"
      @toggle-status="toggleStatus"
      @toggle-favorite="toggleFavorite"
      @toggle-reserve="toggleReserve"
    />

    <RouterView />
  </section>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'

import BookList from '../components/BookList.vue'
import api from '../services/api'

const router = useRouter()

const books = ref([])
const loading = ref(false)

const statusFilter = ref('all')
const sortType = ref('date')

const filteredAndSortedBooks = computed(() => {
  let result = [...books.value]

  if (statusFilter.value === 'available') {
    result = result.filter(book => book.is_available)
  }

  if (sortType.value === 'title') {
    result.sort((a, b) => a.title.localeCompare(b.title))
  }

  if (sortType.value === 'date') {
    result.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
  }

  return result
})

watch(statusFilter, () => {
  console.log('Фильтр изменён:', statusFilter.value)
})

watch(sortType, () => {
  console.log('Сортировка изменена:', sortType.value)
})

async function fetchBooks() {
  loading.value = true

  try {
    const response = await api.get('/books')
    books.value = response.data
  } catch (error) {
    console.error('Ошибка загрузки книг:', error)
  } finally {
    loading.value = false
  }
}

function editBook(id) {
  router.push({ name: 'book-edit', params: { id } })
}

async function deleteBook(id) {
  await api.delete(`/books/${id}`)
  await fetchBooks()
}

async function toggleStatus(id) {
  await api.patch(`/books/${id}/status`)
  await fetchBooks()
}

async function toggleFavorite(id) {
  await api.patch(`/books/${id}/favorite`)
  await fetchBooks()
}

async function toggleReserve(id) {
  await api.patch(`/books/${id}/reserve`)
  await fetchBooks()
}

onMounted(fetchBooks)
</script>