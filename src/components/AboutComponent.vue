<template>
    <MainHeader />
    <section id="team-info">
        <div class="container">
            <div class="row">
                <div v-for="(item, idx) in photoList" v-bind:key="idx" :class="item.class"
                    class="col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="img-area">
                            <img :src="item.src" class="img-fluid" :alt="item.alt">
                        </div>
                        <h4>{{ item.h4 }}</h4>
                        <h5>{{ item.h5 }}</h5>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <MainFooter />
</template>
  
<script>
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

import img1 from "../assets/img/team1.png";
import img2 from "../assets/img/team2.png";
import img3 from "../assets/img/team3.png"

export default {
    name: 'AboutPage',
    components: { MainHeader, MainFooter },
    data() {
        return {
            photoList: [
                { h4: "Виктория Зараменских", h5: "Web Designer", src: img1, class: "", alt: "Зараменских" },
                { h4: "Медиацентр МИЭМ", h5: "Заказчик", src: img3, class: "align-self-center", alt: "Медиацентр" },
                { h4: "Леонид Попов", h5: "Web Designer", src: img2, class: "", alt: "Попов" },
            ]
        };
    }
}
</script>

<style scoped>
/*---- Team ----*/
#team-info {
    padding-top: 5%;

    .card {
        box-shadow: 0px 7px 7px 2px rgba(0, 0, 0, 0.1);
        background-color: rgb(53, 51, 66);
        margin-bottom: 10px;
        margin-left: 10px;
    }

    .card h4 {
        text-align: center;
    }

    .card h5 {
        text-align: center;
    }

    .img-area {
        overflow: hidden;
        position: relative;
    }

    .img-area img {
        width: 100%;
    }

    .img-area:hover img {
        transform: scale(1.2)
    }

    .img-area img {
        transition: all 0.4s ease 0s;
    }

    @media (max-width: 768px) {
        .img-area img {
            display: inline-block;
        }
    }

    .img-area .social ul {
        text-align: center;
        position: relative;
        top: 175px;
    }
}
</style>