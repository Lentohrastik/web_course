import { createApp } from 'vue'
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.css'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
import "bootstrap-icons/font/bootstrap-icons.css"
import 'atropos/css'
import 'chart.js'

//overview pages
import HomeComponent from '/src/components/HomeComponent.vue'
import AboutComponent from '/src/components/AboutComponent.vue'
import DocumentationComponent from '/src/components/DocumentationComponent.vue'
import DownloadComponent from '/src/components/DownloadComponent.vue'
import CVComponent from '/src/components/CVComponent.vue'
import DetailsComponent from '/src/components/DetailsComponent.vue'
import CasparComponent from '/src/components/CasparComponent.vue'
import LearnComponent from '/src/components/LearnComponent.vue'
import ChartComponent from '/src/components/ChartComponent.vue'

//app pages
import AppComponent from '/src/components/AppComponent.vue'
import AddUserComponent from '/src/components/AddUserComponent.vue'
import TemplateComponent from '/src/components/TemplateComponent.vue'
import OBSComponent from '/src/components/OBSComponent.vue'
import DelUserComponent from '/src/components/DelUserComponent.vue'


const router = createRouter({
    history: createWebHistory(),
    routes:[
        //overview paths
        { path: '/', component: HomeComponent},
        { path: '/about', component: AboutComponent},
        { path: '/cv', component: CVComponent},
        { path: '/documentation', component: DocumentationComponent},
        { path: '/download', component: DownloadComponent},
        { path: '/details', component: DetailsComponent},
        { path: '/casparcg', component: CasparComponent},
        { path: '/learn', component: LearnComponent},
        { path: '/charts', component: ChartComponent},

        //app paths
        { path: '/app', component: AppComponent},
        { path: '/app/add_user', component: AddUserComponent},
        { path: '/app/template', component: TemplateComponent},
        { path: '/app/obs', component: OBSComponent},
        { path: '/app/del_user', component: DelUserComponent},
    ]
});


const app = createApp(App)
app.use(bootstrap, router)
app.use(router)
app.mount('#app')

