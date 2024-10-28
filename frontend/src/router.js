// src/router/index.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import UserDashboard from '../src/components/UserDashboard.vue';
import UserLogin from '../src/components/UserLogin.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', redirect: '/login' },  // Redirect root path to login
  { path: '/login', component: UserLogin },
  { path: '/dashboard', component: UserDashboard },
];

const router = new VueRouter({
  mode: 'history',  // Use 'history' mode instead of createWebHistory
  routes,
});

export default router;
