<template>
  <div>
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
  books: Array
})
defineEmits(['edit', 'delete', 'toggle-status', 'toggle-favorite', 'toggle-reserve'])
</script>