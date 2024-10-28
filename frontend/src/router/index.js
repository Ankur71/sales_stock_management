// src/router/index.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import UserDashboard from '../components/Dashboard.vue';
import UserLogin from '../components/UserLogin.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/login', component: UserLogin },
  { path: '/dashboard', component: UserDashboard },
];

const router = new VueRouter({
  mode: 'history', // Use 'history' mode instead of createWebHistory
  routes,
});

export default router;
