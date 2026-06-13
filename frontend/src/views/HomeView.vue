<template>
  <section class="home">
    <div class="home-container">
      <LayoutCard>
        <template #header>
          <div class="header-content">
            <h1>Электронная библиотека ElectoLibrary</h1>
          </div>
        </template>

        <div class="welcome-section">
          <p class="welcome-text">
            Добро пожаловать в ElectoLibrary — удобное приложение для работы с каталогом книг
          </p>
        </div>

        <div class="stats-section">
          <div class="stat-card">
            <div class="stat-number" id="booksCount">0</div>
            <div class="stat-label">книг(и) в каталоге</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">∞</div>
            <div class="stat-label">возможностей</div>
          </div>
          <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">доступ к знаниям</div>
          </div>
        </div>

        <div class="buttons-section">
          <button class="catalog-button" @click="goToCatalog">
            <span>Перейти в электронный каталог</span>
            <svg class="button-icon" viewBox="0 0 24 24" fill="none">
              <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <path d="M12 5L19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
          
          <button class="create-button" @click="goToCreateBook">
            <span>Добавить новую книгу</span>
            <svg class="button-icon" viewBox="0 0 24 24" fill="none">
              <path d="M12 5V19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
      </LayoutCard>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import LayoutCard from '../components/LayoutCard.vue'
import api from '../services/api'

const router = useRouter()

function goToCatalog() {
  router.push({ name: 'books' })
}

function goToCreateBook() {
  router.push({ name: 'book-create' })
}

onMounted(async () => {
  try {
    const response = await api.get('/books')
    const booksCount = response.data.length
    const booksCountElement = document.getElementById('booksCount')
    if (booksCountElement) {
      booksCountElement.textContent = booksCount
    }
  } catch (error) {
    console.error('Ошибка загрузки количества книг:', error)
  }
})
</script>

<style scoped>
.home {
  min-height: 100vh;
  padding: 4rem;
  background: var(--bg);
}

.home-container {
  max-width: 1100px;
  margin: 0 auto;
  width: 100%;
}

.header-content {
  text-align: center;
  margin-bottom: 1rem;
}

h1 {
  font-size: 2.5rem;
  margin: 0;
  line-height: 1.2;
  color: #2c3e50;
}

.welcome-section {
  text-align: center;
  margin-bottom: 2rem;
}

.welcome-text {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #4a5568;
}

.stats-section {
  display: flex;
  justify-content: space-around;
  margin: 2rem 0;
  flex-wrap: wrap;
  gap: 1rem;
}

.stat-card {
  text-align: center;
  padding: 1rem;
  flex: 1;
  min-width: 120px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: #2e3d81;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.9rem;
  color: #718096;
}

.buttons-section {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin: 3rem 0 1rem 0;
  flex-wrap: wrap;
}

.catalog-button,
.create-button {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 12px;
  font-family: inherit;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.catalog-button {
  background: #2e3d81;
  color: white;
  box-shadow: 0 4px 15px rgba(46, 61, 129, 0.3);
}

.catalog-button:hover,
.create-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(46, 61, 129, 0.4);
}

.create-button {
  background: #2e3d81;
  color: white;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.button-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.catalog-button:hover .button-icon,
.create-button:hover .button-icon {
  transform: translateX(5px);
}

.create-button:hover .button-icon {
  transform: rotate(90deg);
}

@media (max-width: 768px) {
  .home {
    padding: 1rem;
  }
  
  .home-container {
    max-width: 100%;
  }
  
  h1 {
    font-size: 1.8rem;
  }
  
  .stats-section {
    flex-direction: column;
    align-items: center;
  }
  
  .stat-card {
    width: 100%;
  }
  
  .buttons-section {
    flex-direction: column;
    gap: 1rem;
  }
  
  .catalog-button,
  .create-button {
    width: 100%;
    justify-content: center;
  }
}
</style>