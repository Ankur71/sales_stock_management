// src/main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router'; 
import 'bootstrap/dist/css/bootstrap.min.css'; 
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css'; 

Vue.config.productionTip = false;

Vue.use(Vuetify); 

new Vue({
    router, 
    vuetify: new Vuetify({
        icons: {
          iconfont: 'mdi', // Specify the icon font
        },
      }),
    render: h => h(App)
}).$mount('#app');
