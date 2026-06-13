<template>
  <article class="book-item">
    <div class="book-cover">
      <img
        v-if="book.cover"
        :src="`http://localhost:8000/${book.cover}`"
        :alt="book.title"
      />
      <div v-else class="cover-placeholder">
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M4 6H20V18H4V6Z" stroke="currentColor" stroke-width="2"/>
          <path d="M8 4V8" stroke="currentColor" stroke-width="2"/>
          <path d="M16 4V8" stroke="currentColor" stroke-width="2"/>
          <path d="M4 10H20" stroke="currentColor" stroke-width="2"/>
        </svg>
      </div>
      
      <div class="badges">
        <span v-if="book.is_favorite" class="badge favorite">❤️</span>
        <span v-if="book.is_reserved" class="badge reserved">🔒</span>
      </div>
    </div>

    <div class="book-info">
      <div class="book-header">
        <h3 class="book-title">{{ book.title }}</h3>
          <div class="status-badge" :class="{ available: book.is_available, unavailable: !book.is_available }">
            <span v-if="book.is_available" class="status-dot"></span>
            <span>{{ book.is_available ? 'В наличии' : 'Нет в наличии' }}</span>
          </div>
      </div>
      
      <div class="book-details">
        <div class="detail-row">
          <svg class="detail-icon" viewBox="0 0 24 24" fill="none">
            <path d="M20 21V19C20 16.8 18.2 15 16 15H8C5.8 15 4 16.8 4 19V21" stroke="currentColor" stroke-width="2"/>
            <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2"/>
          </svg>
          <span>{{ book.author }}</span>
        </div>
        
        <div class="detail-row">
          <svg class="detail-icon" viewBox="0 0 24 24" fill="none">
            <path d="M4 6H20V18H4V6Z" stroke="currentColor" stroke-width="2"/>
            <path d="M8 4V8" stroke="currentColor" stroke-width="2"/>
            <path d="M16 4V8" stroke="currentColor" stroke-width="2"/>
          </svg>
          <span>{{ book.publisher }}</span>
        </div>
        
        <div class="detail-row">
          <svg class="detail-icon" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
            <polyline points="12 6 12 12 16 14" stroke="currentColor" stroke-width="2"/>
          </svg>
          <span>{{ book.year }}</span>
        </div>
        
        <div class="detail-row">
          <svg class="detail-icon" viewBox="0 0 24 24" fill="none">
            <path d="M20 7H4C2.9 7 2 7.9 2 9V19C2 20.1 2.9 21 4 21H20C21.1 21 22 20.1 22 19V9C22 7.9 21.1 7 20 7Z" stroke="currentColor" stroke-width="2"/>
            <path d="M16 21V5C16 3.9 15.1 3 14 3H10C8.9 3 8 3.9 8 5V21" stroke="currentColor" stroke-width="2"/>
          </svg>
          <span>{{ book.category }}</span>
        </div>
      </div>

      <div class="book-actions">
        <button class="action-btn edit" @click="$emit('edit', book.id)" title="Редактировать">
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M17 3L21 7L7 21H3V17L17 3Z" stroke="currentColor" stroke-width="2"/>
          </svg>
        </button>
        
        <button class="action-btn delete" @click="$emit('delete', book.id)" title="Удалить">
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M4 7H20" stroke="currentColor" stroke-width="2"/>
            <path d="M10 11V16" stroke="currentColor" stroke-width="2"/>
            <path d="M14 11V16" stroke="currentColor" stroke-width="2"/>
            <path d="M5 7L6 19C6 20.1 6.9 21 8 21H16C17.1 21 18 20.1 18 19L19 7" stroke="currentColor" stroke-width="2"/>
            <path d="M9 7L10 3H14L15 7" stroke="currentColor" stroke-width="2"/>
          </svg>
        </button>
        
        <button class="action-btn status" @click="$emit('toggle-status', book.id)" title="Изменить статус">
          <svg viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
            <path d="M12 6V12L16 14" stroke="currentColor" stroke-width="2"/>
          </svg>
        </button>
        
        <button class="action-btn favorite" :class="{ active: book.is_favorite }" @click="$emit('toggle-favorite', book.id)" title="Избранное">
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.27 2 8.5 2 5.41 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.08C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.41 22 8.5c0 3.77-3.4 6.86-8.55 11.54L12 21.35Z" stroke="currentColor" :fill="book.is_favorite ? 'currentColor' : 'none'"/>
          </svg>
        </button>
        
        <button class="action-btn reserve" :class="{ active: book.is_reserved }" @click="$emit('toggle-reserve', book.id)" title="Бронирование">
          <svg viewBox="0 0 24 24" fill="none">
            <rect x="3" y="7" width="18" height="14" rx="2" stroke="currentColor" stroke-width="2"/>
            <path d="M8 3V5" stroke="currentColor" stroke-width="2"/>
            <path d="M16 3V5" stroke="currentColor" stroke-width="2"/>
            <path d="M3 11H21" stroke="currentColor" stroke-width="2"/>
          </svg>
        </button>
      </div>
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

<style scoped>
.book-item {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  display: flex;
  gap: 1.5rem;
  padding: 1rem;
}

.book-item:hover {
  transform: translateX(5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

.book-cover {
  position: relative;
  width: 120px;
  height: 160px;
  flex-shrink: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.book-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cover-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.6);
}

.cover-placeholder svg {
  width: 50px;
  height: 50px;
}

.badges {
  position: absolute;
  top: 8px;
  right: 8px;
  display: flex;
  gap: 4px;
}

.badge {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  backdrop-filter: blur(10px);
  background: rgba(0, 0, 0, 0.6);
}

.badge.favorite {
  background: rgba(236, 72, 153, 0.9);
}

.badge.reserved {
  background: rgba(245, 158, 11, 0.9);
}

.book-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.book-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.book-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
  line-height: 1.3;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 500;
  flex-shrink: 0;
}

.status-badge.available {
  background: #dcfce7;
  color: #166534;
}

.status-badge.unavailable {
  background: #fee2e2;
  color: #991b1b;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

.book-details {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  row-gap: 0.5rem;
}

.detail-row {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: #475569;
}

.detail-icon {
  width: 14px;
  height: 14px;
  color: #667eea;
  flex-shrink: 0;
}

.book-actions {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.action-btn {
  width: 32px;
  height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  background: #f1f5f9;
  color: #475569;
}

.action-btn svg {
  width: 16px;
  height: 16px;
}

.action-btn:hover {
  transform: translateY(-2px);
}

.action-btn.edit:hover {
  background: #e0e7ff;
  color: #4338ca;
}

.action-btn.delete:hover {
  background: #fee2e2;
  color: #dc2626;
}

.action-btn.status:hover {
  background: #e0f2fe;
  color: #0284c7;
}

.action-btn.favorite {
  background: #fce7f3;
  color: #db2777;
}

.action-btn.favorite.active {
  background: #fbcfe8;
  color: #be185d;
}

.action-btn.favorite:hover {
  background: #fbcfe8;
}

.action-btn.reserve {
  background: #fef3c7;
  color: #d97706;
}

.action-btn.reserve.active {
  background: #fde68a;
  color: #b45309;
}

.action-btn.reserve:hover {
  background: #fde68a;
}

@media (max-width: 768px) {
  .book-item {
    flex-direction: column;
    padding: 0.75rem;
    gap: 1rem;
  }
  
  .book-cover {
    width: 100%;
    height: 200px;
  }
  
  .book-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .book-details {
    gap: 0.5rem;
  }
  
  .action-btn {
    width: 36px;
    height: 36px;
  }
}
</style>