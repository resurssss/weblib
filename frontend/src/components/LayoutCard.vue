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

<style scoped>
.layout-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.layout-card-header {
  margin-bottom: 1rem;
}

.layout-card-body {
  margin-bottom: 1.5rem;
}

.layout-card-footer {
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
  color: #64748b;
  font-size: 0.9rem;
}
</style>