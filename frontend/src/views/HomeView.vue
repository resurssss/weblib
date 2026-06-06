<template>
  <section class="home">
    <LayoutCard>
      <template #header>
        <h1>Электронная библиотека</h1>
      </template>

      <p>
        Добро пожаловать в ElectoLibrary — SPA-приложение для работы с каталогом книг.
      </p>

      <template #footer="{ createdAt }">
        <p>Карточка создана: {{ createdAt }}</p>

        <button @click="goToCatalog">
          Электронный каталог
        </button>
      </template>
    </LayoutCard>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
import LayoutCard from '../components/LayoutCard.vue'

const router = useRouter()

function goToCatalog() {
  router.push({ name: 'books' })
}
</script>