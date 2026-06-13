<template>
  <section class="catalog-page">
    <div class="catalog-container">
      <h4 class="catalog-title">Каталог книг</h4>

      <div class="controls">
        <div class="filter-group">
          <label>Фильтр по статусу:</label>
          <select v-model="statusFilter" class="custom-select">
            <option value="all">Все</option>
            <option value="available">В наличии</option>
          </select>
        </div>

        <div class="filter-group">
          <label>Сортировка:</label>
          <select v-model="sortType" class="custom-select">
            <option value="date">По дате добавления</option>
            <option value="title">По алфавиту</option>
          </select>
        </div>
      </div>

      <div class="stats">
        <p>Найдено книг: {{ filteredAndSortedBooks.length }}</p>
      </div>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Загрузка...</p>
      </div>

      <div v-else-if="filteredAndSortedBooks.length === 0" class="empty-state">
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M4 6H20V18H4V6Z" stroke="currentColor" stroke-width="2"/>
          <path d="M8 4V8" stroke="currentColor" stroke-width="2"/>
          <path d="M16 4V8" stroke="currentColor" stroke-width="2"/>
        </svg>
        <p>Список книг пуст</p>
      </div>

      <div v-else class="books-grid">
        <BookItem
          v-for="book in filteredAndSortedBooks"
          :key="book.id"
          :book="book"
          @edit="editBook"
          @delete="deleteBook"
          @toggle-status="toggleStatus"
          @toggle-favorite="toggleFavorite"
          @toggle-reserve="toggleReserve"
        />
      </div>
    </div>

    <RouterView />
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

import BookItem from '../components/BookItem.vue'
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
  if (confirm('Вы уверены, что хотите удалить эту книгу?')) {
    await api.delete(`/books/${id}`)
    await fetchBooks()
  }
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

<style scoped>
.catalog-page {
  min-height: 100vh;
  padding: 1rem;
}

.catalog-title {
  font-size: 2rem;
  color: #2e3d81;
  text-align: left;
  margin: 1rem 0 2rem 1rem; 
  font-weight: 600;
  /*text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);*/
}

.catalog-container {
  max-width: 1400px;
  margin: 0 auto;
  width: 80%;
}

.controls {
  display: flex;
  justify-content: left;
  gap: 2rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(255, 255, 255, 0.95);
  padding: 0.5rem 0.5rem;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.filter-group label {
  font-weight: 500;
  color: #1e293b;
}

.custom-select {
  padding: 0.4rem 0.8rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: white;
  color: #1e293b;
  font-family: inherit;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.custom-select:hover {
  border-color: #667eea;
}

.custom-select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.stats {
  text-align: left;
  margin-bottom: 0rem;
}

.stats p {
  display: inline-block;
  background: rgba(255, 255, 255, 0.95);
  padding: 0.5rem 1.5rem;
  border-radius: 40px;
  color: #1e293b;
  font-weight: 500;
  font-size: 0.9rem;
}

.loading {
  text-align: center;
  padding: 4rem;
  color: white;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.empty-state {
  text-align: center;
  padding: 4rem;
  color: white;
}

.empty-state svg {
  width: 80px;
  height: 80px;
  margin: 0 auto 1rem;
  color: rgba(255, 255, 255, 0.6);
}

.empty-state p {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.8);
}

.books-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

@media (min-width: 1024px) {
  .books-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
}

@media (max-width: 768px) {
  .catalog-page {
    padding: 1rem;
  }
  
  .catalog-title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .controls {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .filter-group {
    justify-content: space-between;
    width: 100%;
  }
  
  .books-grid {
    gap: 0.75rem;
  }
}
</style>