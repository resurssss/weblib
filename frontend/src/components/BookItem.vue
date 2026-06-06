<template>
  <article class="book-item">

    <div v-if="book.cover">
      <img
        :src="`http://localhost:8000/${book.cover}`"
        :alt="book.title"
        width="180"
      />
    </div>

    <h3>{{ book.title }}</h3>

    <p><b>Автор:</b> {{ book.author }}</p>
    <p><b>Издательство:</b> {{ book.publisher }}</p>
    <p><b>Год:</b> {{ book.year }}</p>
    <p><b>Категория:</b> {{ book.category }}</p>
    <p><b>Подборка:</b> {{ book.collection || 'Без подборки' }}</p>

    <p>
      <b>Статус:</b>
      <span v-if="book.is_available">в наличии</span>
      <span v-else>нет в наличии</span>
    </p>

    <p>
      <b>Избранное:</b>
      <span>{{ book.is_favorite ? 'да' : 'нет' }}</span>
    </p>

    <p>
      <b>Бронь:</b>
      <span>{{ book.is_reserved ? 'забронирована' : 'свободна' }}</span>
    </p>

    <div class="book-actions">
      <button @click="$emit('edit', book.id)">Редактировать</button>
      <button @click="$emit('delete', book.id)">Удалить</button>
      <button @click="$emit('toggle-status', book.id)">Изменить статус</button>
      <button @click="$emit('toggle-favorite', book.id)">
        {{ book.is_favorite ? 'Убрать ❤️' : 'В избранное ❤️' }}
      </button>
      <button @click="$emit('toggle-reserve', book.id)">
        {{ book.is_reserved ? 'Отменить бронь' : 'Забронировать' }}
      </button>
    </div>
  </article>
</template>

<script setup>
defineProps({
  book: {
    type: Object,
    required: true
  }
})

defineEmits([
  'edit',
  'delete',
  'toggle-status',
  'toggle-favorite',
  'toggle-reserve'
])
</script>