import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
// import AdversarialView from '../views/AdversarialView.vue'
// import UserView from '../views/UserView.vue'

// import Axios from 'axios'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainview',
    component: MainView,
  },
]

const router = new VueRouter({
  routes
})

export default router
