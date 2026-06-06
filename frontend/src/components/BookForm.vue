<template>
  <form class="book-form" @submit.prevent="submitForm">
    <div>
      <label>Заголовок</label>
      <input
        ref="titleInput"
        v-model.trim="form.title"
        type="text"
        placeholder="Введите заголовок книги"
      />
      <small v-if="errors.title">{{ errors.title }}</small>
    </div>

    <div>
      <label>Автор</label>
      <input
        v-model.trim="form.author"
        type="text"
        placeholder="Введите автора"
      />
      <small v-if="errors.author">{{ errors.author }}</small>
    </div>

    <div>
      <label>Описание</label>
      <textarea
        v-model.trim="form.description"
        placeholder="Введите описание книги"
      ></textarea>
      <small v-if="errors.description">{{ errors.description }}</small>
    </div>

    <div>
      <label>Обложка JPG</label>
      <input
        type="file"
        accept=".jpg,.jpeg"
        @change="handleFileChange"
      />
      <small v-if="errors.cover">{{ errors.cover }}</small>
    </div>

    <div>
      <label>Издательство</label>
      <select v-model="form.publisher">
        <option value="">Выберите издательство</option>
        <option value="АСТ">АСТ</option>
        <option value="Эксмо">Эксмо</option>
        <option value="Азбука">Азбука</option>
        <option value="Росмэн">Росмэн</option>
        <option value="Питер">Питер</option>
      </select>
      <small v-if="errors.publisher">{{ errors.publisher }}</small>
    </div>

    <div>
      <label>Категория / возрастной рейтинг</label>

      <label>
        <input v-model="form.category" type="radio" value="0+" />
        0+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="6+" />
        6+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="12+" />
        12+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="16+" />
        16+
      </label>

      <label>
        <input v-model="form.category" type="radio" value="18+" />
        18+
      </label>

      <small v-if="errors.category">{{ errors.category }}</small>
    </div>

    <div>
      <label>Год издания</label>
      <input
        v-model.number="form.year"
        type="number"
        placeholder="Например, 2020"
      />
      <small v-if="errors.year">{{ errors.year }}</small>
    </div>

    <div>
      <label>Подборка по тематике</label>
      <input
        v-model.trim="form.collection"
        type="text"
        placeholder="Например, русская классика"
      />
    </div>

    <button type="submit">
      {{ submitText }}
    </button>
  </form>
</template>

<script setup>
import { reactive, ref, watch, onMounted } from 'vue'

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