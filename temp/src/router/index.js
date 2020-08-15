import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import BlogList from '../views/BlogList.vue'
import NewBlog from '../views/NewBlog.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/bloglist',
    name: 'BlogList',
    component: BlogList
  },
  {
    path: '/newblog',
    name: 'NewBlog',
    component: NewBlog
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
