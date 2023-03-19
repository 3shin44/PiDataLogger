import { createApp } from 'vue'
import App from './App.vue'
const app = createApp(App)

// bootstrap 
import 'bootstrap/dist/css/bootstrap.min.css'

// import custom css (note: higher version of sass-loader causes error, v10 is compatible )
import '@/assets/css/index.scss'

import VueApexCharts from "vue3-apexcharts";
app.use(VueApexCharts)

app.mount('#app')
