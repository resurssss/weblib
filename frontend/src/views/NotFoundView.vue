<template>
  <section class="not-found-page">
    <div class="not-found-container">
      <h1 class="error-code">404</h1>
      <h2 class="error-title">Страница не найдена</h2>
      <p class="error-text">
        Такой страницы в ElectoLibrary не существует
      </p>
      <div class="buttons-group">
        <button class="home-button" @click="goHome">
          На главную
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goHome() {
  router.push({ name: 'home' })
}

function goBooks() {
  router.push({ name: 'books' })
}
</script>

<style scoped>
.not-found-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  padding: 0rem;
}

.not-found-container {
  text-align: center;
  max-width: 600px;
  width: 100%;
}

.error-code {
  font-size: 6rem;
  font-weight: 800;
  color: #1e293b;
  margin: 3rem 0rem 3rem;
  line-height: 1;
  padding: 10;
}

.error-title {
  font-size: 2rem;
  color: #1e293b;
  margin: 0.5rem 0;
  font-weight: 600;
}

.error-text {
  font-size: 1rem;
  color: #718096;
  margin-bottom: 3rem;
}

.buttons-group {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.home-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.9rem 2rem;
  border: none;
  border-radius: 12px;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
  background: #2e3d81;
  color: white;
}

.home-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(46, 61, 129, 0.3);
}

@media (max-width: 768px) {
  .error-code {
    font-size: 5rem;
  }
  
  .error-title {
    font-size: 1.5rem;
  }
  
  .buttons-group {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .home-button,
  .catalog-button {
    width: 100%;
    justify-content: center;
  }
}
</style>