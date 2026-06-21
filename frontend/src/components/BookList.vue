<template>
  <div class="books-grid">
    <BookItem
      v-for="book in books"
      :key="book.id"
      :book="book"
      @edit="$emit('edit', $event)"
      @delete="$emit('delete', $event)"
      @toggle-status="$emit('toggle-status', $event)"
      @toggle-favorite="$emit('toggle-favorite', $event)"
      @toggle-reserve="$emit('toggle-reserve', $event)"
    />
  </div>
</template>

<script setup>
import BookItem from './BookItem.vue'

defineProps({
  books: {
    type: Array,
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

<style scoped>
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
</style>