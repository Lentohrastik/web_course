<template>
    <AppHeader />
    <main>
        <div class="pb-3 text-center text-white">
            <h2>Окно Выбора шаблона</h2>
            <p>Выбирете шаблон, кликнув по нему и нажмите кнопку отправить!</p>
        </div>

        <div class="card-group pb-5">
            <div v-for="(item, idx) in photoExaples" v-bind:key="idx" :class="item.class" class="card"
                @click="chooseTemplate(idx)">
                <img :src="item.src" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5>{{ item.text }}</h5>
                </div>
            </div>
        </div>



        <div class="p-5 d-flex justify-content-center">
            <div class="btn btn-primary btn-rounded" @click="sendTemplate">
                <i class="fs-4 bi-send-fill text-white"></i>
                <span class="ms-1 d-none d-sm-inline text-white">
                    <label class="form-label text-white m-1">Отправить</label>
                </span>
            </div>
        </div>

        <div v-show="isShow" class="alert alert-info text-center" role="alert">
            Шаблон выбран!
        </div>
    </main>
    <MainFooter />
</template>
  
<script>
import AppHeader from './AppHeader.vue';
import MainFooter from './MainFooter.vue';

import img1 from "../assets/img/pic01.png";
import img2 from "../assets/img/pic02.png";
import img3 from "../assets/img/pic03.png";

export default {
    name: 'TemplatePage',
    components: { AppHeader, MainFooter },

    data() {
        return {
            photoExaples: [
                { text: "Шаблон 1", src: img1, class: "choosen" },
                { text: "Шаблон 2", src: img2, class: "" },
                { text: "Шаблон 3", src: img3, class: "" },
            ],
            isShow: false,
        };
    },

    methods: {
        chooseTemplate(idx) {
            for (const i in [0, 1, 2]) {
                if (i == idx) {
                    this.photoExaples[i].class = "choosen";
                }
                else {
                    this.photoExaples[i].class = "";
                }
            }
        },

        sendTemplate() {
            for (const i in [0, 1, 2]) {
                this.photoExaples[i].class = "";
            }
            this.photoExaples[0].class = "choosen";
            this.isShow = true;
            setTimeout(() => {
                this.isShow = false;
            }, 5000)
        },
    }
}
</script>

<style scoped>
.choosen {
    background-color: #364647;
}
</style>