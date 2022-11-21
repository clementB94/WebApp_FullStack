import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import axios from 'axios'

import './assets/main.css'



// axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // the FastAPI backend


const app = createApp(App)
app.use(createPinia())
app.use(router)



app.mount('#app')
