<template>
  <div class="book-item">
    <h3>{{ book.title }}</h3>
    <p>Автор: {{ book.author }}</p>
    <p>Издательство: {{ book.publisher }}</p>
    <p>Год: {{ book.year }}</p>
    <p>Категория: {{ book.category }}</p>
    <p>Коллекция: {{ book.collection }}</p>

    <button @click="$emit('edit', book.id)">Редактировать</button>
    <button @click="$emit('delete', book.id)">Удалить</button>
    <button @click="$emit('toggle-status', book.id)">
      {{ book.is_available ? 'Снять с полки' : 'Доступно' }}
    </button>
    <button @click="$emit('toggle-favorite', book.id)">
      {{ book.is_favorite ? '💔' : '❤️' }}
    </button>
    <button @click="$emit('toggle-reserve', book.id)">
      {{ book.is_reserved ? 'Отменить бронь' : 'Забронировать' }}
    </button>
  </div>
</template>

<script setup>
defineProps({
  book: Object
})
defineEmits(['edit', 'delete', 'toggle-status', 'toggle-favorite', 'toggle-reserve'])
</script>