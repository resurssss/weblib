<template>
  <section class="layout-card">
    <header class="layout-card-header">
      <slot name="header">
        <h2>Заголовок карточки</h2>
      </slot>
    </header>

    <main class="layout-card-body">
      <slot>
        <p>Основное содержимое карточки</p>
      </slot>
    </main>

    <footer class="layout-card-footer">
      <slot name="footer" :created-at="createdAt">
        <p>Дата не указана</p>
      </slot>
    </footer>
  </section>
</template>

<script setup>
const createdAt = new Date().toLocaleDateString('ru-RU')
</script>