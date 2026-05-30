<template>
  <div class="app">
    <header class="header">
      <h1>Электронная библиотека</h1>
      <p>Ваша персональная коллекция книг</p>
    </header>
    
    <div class="container">
      <!-- Форма добавления книги (POST) -->
      <div class="card add-card">
        <h2>Добавить новую книгу</h2>
        <form @submit.prevent="addBook">
          <div class="form-group">
            <input 
              v-model="newBook.title" 
              type="text" 
              placeholder="Название книги"
              required
            />
          </div>
          <div class="form-group">
            <input 
              v-model="newBook.author" 
              type="text" 
              placeholder="Автор"
              required
            />
          </div>
          <button type="submit" class="btn btn-primary">
            <span>➕</span> Добавить книгу
          </button>
        </form>
      </div>

      <!-- Список книг (GET) -->
      <div class="card list-card">
        <div class="card-header">
          <h2>Мои книги</h2>
          <span class="badge">{{ books.length }} книг</span>
        </div>
        
        <div v-if="loading" class="loading">
          <div class="spinner"></div>
          <p>Загрузка...</p>
        </div>
        
        <div v-else-if="books.length === 0" class="empty">
          <p>Пока нет книг</p>
          <p class="empty-hint">Добавьте первую книгу выше</p>
        </div>
        
        <ul v-else class="books-list">
          <li v-for="book in books" :key="book.id" class="book-item">
            <div class="book-details">
              <div class="book-title">{{ book.title }}</div>
              <div class="book-author">{{ book.author }}</div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const books = ref([])
const loading = ref(false)
const newBook = ref({ title: '', author: '' })

// GET запрос
const fetchBooks = async () => {
  loading.value = true
  try {
    const response = await fetch('/api/books')
    const data = await response.json()
    books.value = data
  } catch (error) {
    console.error('Ошибка:', error)
  } finally {
    loading.value = false
  }
}

// POST запрос
const addBook = async () => {
  if (!newBook.value.title || !newBook.value.author) return
  
  try {
    const response = await fetch('/api/books', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newBook.value),
    })
    const data = await response.json()
    books.value.push(data)
    newBook.value = { title: '', author: '' }
  } catch (error) {
    console.error('Ошибка:', error)
  }
}

onMounted(() => {
  fetchBooks()
})
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.app {
  min-height: 100vh;
  background: linear-gradient(135deg, #abb6e6 0%, #d2bbea 100%);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

.header {
  text-align: center;
  padding: 40px 20px;
  color: white;
}

.header h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
  font-weight: 500;
  color: #492174;
}

.header p {
  font-size: 1.1rem;
  opacity: 0.9;
  color: #250848;
}

.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px 40px;
}

.card {
  background: white;
  border-radius: 20px;
  padding: 30px;
  margin-bottom: 30px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 30px 50px rgba(0, 0, 0, 0.15);
}

.add-card {
  background: linear-gradient(135deg, #fff 0%, #f8f9ff 100%);
}

.add-card h2 {
  color: #492174;
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.form-group {
  margin-bottom: 15px;
}

.form-group input {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 15px;
  transition: all 0.3s ease;
  font-family: inherit;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.btn {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
}

.btn-primary {
  background: linear-gradient(135deg, #ac93eb 0%, #894ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

.btn-primary span {
  margin-right: 8px;
}

.list-card {
  background: white;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 2px solid #f0f0f0;
}

.card-header h2 {
  color: #333;
  font-size: 1.5rem;
}

.badge {
  background: linear-gradient(135deg, #ac93eb 0%, #894ba2 100%);
  color: white;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
}

.books-list {
  list-style: none;
}

.book-item {
  display: flex;
  align-items: center;
  padding: 15px;
  margin-bottom: 10px;
  background: #f8f9fa;
  border-radius: 12px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.book-item:hover {
  background: #f0f2f5;
  transform: translateX(5px);
}

.book-icon {
  font-size: 2rem;
  margin-right: 15px;
}

.book-details {
  flex: 1;
}

.book-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 5px;
}

.book-author {
  font-size: 0.9rem;
  color: #667eea;
}

.loading {
  text-align: center;
  padding: 40px;
}

.spinner {
  width: 40px;
  height: 40px;
  margin: 0 auto 15px;
  border: 3px solid #f0f0f0;
  border-top: 3px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.empty {
  text-align: center;
  padding: 40px;
  color: #999;
}

.empty p {
  margin: 5px 0;
}

.empty-hint {
  font-size: 0.9rem;
  opacity: 0.7;
}

@media (max-width: 768px) {
  .header h1 {
    font-size: 1.8rem;
  }
  
  .card {
    padding: 20px;
  }
  
  .book-title {
    font-size: 1rem;
  }
}
</style>