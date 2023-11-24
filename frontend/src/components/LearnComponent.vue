<template>
    <MainHeader />

    <div id="carouselExampleCaptions" class="carousel carousel-dark slide p-5" data-bs-ride="false">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
                aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
                aria-label="Slide 2"></button>
        </div>
        <div class="carousel-inner">
            <div v-for="(item, idx) in carouselList" v-bind:key="idx" :class="item.class" class="carousel-item">
                <div class="card-group container">
                    <div v-for="(item2, idx) in item.list" v-bind:key="idx" class="card col col-lg-4">
                        <LiteYouTubeEmbed :id="item2.src" title="CasparCG for Live Production" />
                        <div class="card-body">
                            <h5 class="card-title">{{ item2.title }}</h5>
                            <p class="card-text">{{ item2.text }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>

    <div class="container text-center">
        <h6>В данном разделе вы можете ознакомиться с обучающими роликами по Автоматической Титровальной Системе. </h6>
    </div>

    <MainFooter />
</template>
  
<script>
import LiteYouTubeEmbed from 'vue-lite-youtube-embed'
import 'vue-lite-youtube-embed/style.css'

import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {

    name: 'LearnPage',
    components: { MainHeader, MainFooter, LiteYouTubeEmbed },
    data() {
        return {
            carouselList: [
                {
                    list: [
                        { title: "CasparCG for Live Production", text: "Обзорное видео с возможностями CasparCG, использование шаблонов, разных источников и пр.", src: "Sc3yKYc6gsI" },
                        { title: "CasparCG First Steps", text: "Начните работать с CasparCG без проблем.", src: "sMCyBE60Dao" },
                        { title: "Create Template by Loopic", text: "Создавайте шаблоны для CasparCG с помощью веб-приложения Loopic без необходимости разбираться в html коде.", info: "info", src: "gZRYTmngqLw" },
                    ],
                    class: "active",
                },
                {
                    list: [
                        { title: "Распознавание лиц на Python", text: "В данном видео пишем программу для распознавания лиц на изображениях с помощью Python. Научимся находить, сверять, выделять и экспортировать лица людей используя библиотеки Face Recognition и Pillow.", src: "RUez4WJ1Vpo" },
                        { title: "Live Face Recognition in Python", text: "В этом видео: как реализовать систему распознавания лиц в реальном времени на Python с использованием машинного обучения и OpenCV.", src: "pQvkoaevVMk" },
                        { title: "How does facial recognition work?", text: "Обзорное видео о биометрической технологии распознавания лица.", info: "info", src: "YX8BzK_LU0E" },
                    ],
                    class: "",
                }
            ]
        };
    }
}
</script>

<style scoped>
.carousel-control-next,
.carousel-control-prev {
    filter: invert(100%);
}

.carousel-indicators {
    filter: invert(100%);
}
</style>