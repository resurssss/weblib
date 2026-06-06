<template>
  <section class="not-found-page">
    <h1>404</h1>

    <h2>Страница не найдена</h2>

    <p>
      Такой страницы в ElectoLibrary не существует.
    </p>

    <button @click="goHome">
      На главную
    </button>

    <button @click="goBooks">
      В электронный каталог
    </button>
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