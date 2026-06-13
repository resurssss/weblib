<template>
  <form class="book-form" @submit.prevent="submitForm">
    <div class="form-group">
      <label>Заголовок</label>
      <input
        ref="titleInput"
        v-model.trim="form.title"
        type="text"
        placeholder="Введите заголовок книги"
      />
      <small v-if="errors.title" class="error">{{ errors.title }}</small>
    </div>

    <div class="form-group">
      <label>Автор</label>
      <input
        v-model.trim="form.author"
        type="text"
        placeholder="Введите автора"
      />
      <small v-if="errors.author" class="error">{{ errors.author }}</small>
    </div>

    <div class="form-group">
      <label>Описание</label>
      <textarea
        v-model.trim="form.description"
        placeholder="Введите описание книги"
        rows="4"
      ></textarea>
      <small v-if="errors.description" class="error">{{ errors.description }}</small>
    </div>

    <div class="form-group">
      <label>Обложка JPG</label>
      <input
        type="file"
        accept=".jpg,.jpeg"
        @change="handleFileChange"
      />
      <small v-if="errors.cover" class="error">{{ errors.cover }}</small>
    </div>

    <div class="form-group">
      <label>Издательство</label>
      <select v-model="form.publisher">
        <option value="">Выберите издательство</option>
        <option value="АСТ">АСТ</option>
        <option value="Эксмо">Эксмо</option>
        <option value="Азбука">Азбука</option>
        <option value="Росмэн">Росмэн</option>
        <option value="Питер">Питер</option>
      </select>
      <small v-if="errors.publisher" class="error">{{ errors.publisher }}</small>
    </div>

    <div class="form-group">
      <label>Категория / возрастной рейтинг</label>
      <div class="radio-group">
        <label class="radio-label">
          <input v-model="form.category" type="radio" value="0+" />
          <span>0+</span>
        </label>

        <label class="radio-label">
          <input v-model="form.category" type="radio" value="6+" />
          <span>6+</span>
        </label>

        <label class="radio-label">
          <input v-model="form.category" type="radio" value="12+" />
          <span>12+</span>
        </label>

        <label class="radio-label">
          <input v-model="form.category" type="radio" value="16+" />
          <span>16+</span>
        </label>

        <label class="radio-label">
          <input v-model="form.category" type="radio" value="18+" />
          <span>18+</span>
        </label>
      </div>
      <small v-if="errors.category" class="error">{{ errors.category }}</small>
    </div>

    <div class="form-group">
      <label>Год издания</label>
      <input
        v-model.number="form.year"
        type="number"
        placeholder="Например, 2020"
      />
      <small v-if="errors.year" class="error">{{ errors.year }}</small>
    </div>

    <div class="form-group">
      <label>Подборка по тематике</label>
      <input
        v-model.trim="form.collection"
        type="text"
        placeholder="Например, русская классика"
      />
    </div>

    <div class="form-actions">
      <button type="submit" class="btn-submit">
        {{ submitText }}
      </button>
    </div>
  </form>
</template>

<script setup>
import { reactive, ref, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const props = defineProps({
  initialBook: {
    type: Object,
    default: null
  },
  submitText: {
    type: String,
    default: 'Сохранить'
  }
})

const emit = defineEmits(['submit'])

const titleInput = ref(null)

const form = reactive({
  title: '',
  author: '',
  description: '',
  cover: null,
  publisher: '',
  category: '',
  year: null,
  collection: ''
})

const errors = reactive({
  title: '',
  author: '',
  description: '',
  cover: '',
  publisher: '',
  category: '',
  year: ''
})

onMounted(() => {
  if (titleInput.value) {
    titleInput.value.focus()
  }
})

watch(
  () => props.initialBook,
  (book) => {
    if (book) {
      form.title = book.title || ''
      form.author = book.author || ''
      form.description = book.description || ''
      form.publisher = book.publisher || ''
      form.category = book.category || ''
      form.year = book.year || null
      form.collection = book.collection || ''
    }
  },
  { immediate: true }
)

function handleFileChange(event) {
  const file = event.target.files[0]

  if (!file) {
    form.cover = null
    return
  }

  const isJpg = file.type === 'image/jpeg'

  if (!isJpg) {
    errors.cover = 'Можно загрузить только файл JPG'
    form.cover = null
    return
  }

  errors.cover = ''
  form.cover = file
}

function validateForm() {
  errors.title = ''
  errors.author = ''
  errors.description = ''
  errors.publisher = ''
  errors.category = ''
  errors.year = ''

  let isValid = true

  if (!form.title) {
    errors.title = 'Введите заголовок книги'
    isValid = false
  }

  if (!form.author) {
    errors.author = 'Введите автора'
    isValid = false
  }

  if (!form.description) {
    errors.description = 'Введите описание'
    isValid = false
  }

  if (!form.publisher) {
    errors.publisher = 'Выберите издательство'
    isValid = false
  }

  if (!form.category) {
    errors.category = 'Выберите категорию'
    isValid = false
  }

  if (!form.year || form.year < 1000 || form.year > new Date().getFullYear()) {
    errors.year = 'Введите корректный год издания'
    isValid = false
  }

  return isValid
}


function submitForm() {
  if (!validateForm()) return

  const formData = new FormData()

  formData.append('title', form.title)
  formData.append('author', form.author)
  formData.append('description', form.description)
  formData.append('publisher', form.publisher)
  formData.append('category', form.category)
  formData.append('year', form.year)
  formData.append('collection', form.collection)

  if (form.cover) {
    formData.append('cover', form.cover)
  }

  emit('submit', formData)
}
</script>

<style scoped>
.book-form {
  padding: 2rem;
}

.form-group {
  margin-bottom: 2rem;
}

.form-group label {
  display: block;
  text-align: left;
  margin-bottom: 0.75rem;
  font-weight: 500;
  color: #1e293b;
  font-size: 0.95rem;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1rem;
  font-family: inherit;
  transition: all 0.2s ease;
  background: #f8fafc;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  background: white;
}

.form-group input:hover,
.form-group textarea:hover,
.form-group select:hover {
  border-color: #cbd5e1;
}

.form-group input[type="file"] {
  padding: 0.75rem;
  border: 1px dashed #e2e8f0;
  background: #f8fafc;
  cursor: pointer;
}

.form-group input[type="file"]:hover {
  border-color: #667eea;
  background: #f1f5f9;
}

/* Radio группа */
.radio-group {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}

.radio-label {
  display: inline-flex !important;
  align-items: center;
  gap: 0.5rem;
  font-weight: normal !important;
  margin-bottom: 0 !important;
  cursor: pointer;
  font-size: 0.95rem;
}

.radio-label input[type="radio"] {
  width: auto;
  margin: 0;
  cursor: pointer;
}

.radio-label span {
  color: #475569;
}

.radio-label:hover span {
  color: #667eea;
}

/* Ошибки */
.error {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: #dc2626;
}

/* Кнопки */
.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn-submit {
  flex: 1;
  padding: 0.875rem;
  border: none;
  max-width: 300px;
  margin: 0 auto 2rem auto; /* 2rem отступ снизу */
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
  background: #2e3d81;
  color: white;
}


.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.btn-cancel:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
}

.btn-submit:active,
.btn-cancel:active {
  transform: translateY(0);
}

@media (max-width: 768px) {
  .book-form {
    padding: 1.5rem;
  }
  
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  .radio-group {
    gap: 1rem;
  }
  
  .form-actions {
    flex-direction: column;
    gap: 0.75rem;
  }
}
</style>