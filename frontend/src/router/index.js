import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import BooksView from '../views/BooksView.vue'
import CreateBookView from '../views/CreateBookView.vue'
import EditBookView from '../views/EditBookView.vue'
import NotFoundView from '../views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/books',
      name: 'books',
      component: BooksView
    },
    {
      path: '/books/new',
      name: 'book-create',
      component: CreateBookView
    },
    {
      path: '/books/:id/edit',
      name: 'book-edit',
      component: EditBookView,
      props: true
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFoundView
    }
  ]
})

export default router