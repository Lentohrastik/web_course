<template>
    <MainHeader />
    <main>

        <div class="card-group">
            <div v-for="(value, idx) in chartsList" v-bind:key="idx" class="card col col-lg-4">
                <component v-bind:is="value.component" :data="value.data" :options="options" />
                <div class="card-body">
                    <h5 class="card-title">{{ value.head }}</h5>
                    <p class="card-text">{{ value.text }}</p>
                </div>
            </div>
        </div>
        <div class="card-group">
            <div v-for="(value, idx) in chartsList2" v-bind:key="idx" class="card col col-lg-4">
                <component v-bind:is="value.component" :data="value.data" :options="options" />
                <div class="card-body">
                    <h5 class="card-title">{{ value.head }}</h5>
                    <p class="card-text">{{ value.text }}</p>
                </div>
            </div>
        </div>

    </main>
    <MainFooter />
</template>
  
<script >
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    BarElement,
    RadialLinearScale,
    ArcElement,
} from 'chart.js'
import { Line, Bar, PolarArea } from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    BarElement,
    RadialLinearScale,
    ArcElement
)

export default {
    name: 'ChartPage',
    components: { MainHeader, MainFooter, Line, Bar, PolarArea },

    data() {
        return {
            chartsList: [
                {
                    head: "",
                    text: "",
                    component: "Bar",
                    data: {
                        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                        datasets: [
                            {
                                label: 'Data One',
                                backgroundColor: '#f87979',
                                data: [40, 39, 10, 40, 39, 80, 40]
                            },
                            {
                                label: 'Data Two',
                                backgroundColor: '#ffffff',
                                data: [45, 40, 10, 40, 39, 80, 40]
                            }
                        ]
                    },
                },
                {
                    head: "",
                    text: "",
                    component: "Line",
                    data: {
                        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                        datasets: [
                            {
                                label: 'Data One',
                                backgroundColor: '#f87979',
                                data: [40, 39, 10, 40, 39, 80, 40]
                            }
                        ]
                    },
                },
                {
                    head: "",
                    text: "",
                    component: "PolarArea",
                    data: {
                        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                        datasets: [
                            {
                                label: 'Data One',
                                backgroundColor: '#f87979',
                                data: [40, 39, 10, 40, 39, 80, 40]
                            }
                        ]
                    },
                },
            ],

            chartsList2: [
                {
                    head: "",
                    text: "",
                    component: "Bar",
                    data: {
                        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                        datasets: [
                            {
                                label: 'Data One',
                                backgroundColor: '#f87979',
                                data: [40, 39, 10, 40, 39, 80, 40]
                            },
                            {
                                label: 'Data Two',
                                backgroundColor: '#ffffff',
                                data: [45, 40, 10, 40, 39, 80, 40]
                            }
                        ]
                    },
                },
                {
                    head: "",
                    text: "",
                    component: "Line",
                    data: {
                        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                        datasets: [
                            {
                                label: 'Data One',
                                backgroundColor: '#f87979',
                                data: [40, 39, 10, 40, 39, 80, 40]
                            }
                        ]
                    },
                },
            ],


            options: {
                responsive: true,
                maintainAspectRatio: true,
            }
        }
    }
}
</script>