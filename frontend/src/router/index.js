import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/list',
      name: 'list',
      component: () => import('../views/MoviesListView.vue')
    },
    {
      path: '/movie/:id',
      name: 'movie',
      props: true,
      component: () => import('../views/MovieView.vue')
    },
    {
      path: '/profil/:id',
      name: 'profil',
      props: true,
      component: () => import('../views/ProfilView.vue')
    },
    {
      path: '/scraping',
      name: 'scraping',
      component: () => import('../views/ScrapingView.vue')
    },
  ]
})

export default router
