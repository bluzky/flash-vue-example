import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from './utils/axios';
const app = createApp(App);

app.use(router);
app.use(axios, {
  baseUrl: import.meta.env.VITE_API_ENDPOINT
});

// provide axios so we can use it in composition component
app.provide('axios', app.config.globalProperties.axios);
app.mount('#app');
