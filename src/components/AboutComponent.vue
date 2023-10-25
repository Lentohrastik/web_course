<template>
    <MainHeader />
    <section id="team-info">
        <div class="container">
            <div class="row">
                <div class="col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="img-area">
                            <img src="../assets/img/team1.png" class="img-fluid" alt="Зараменских">
                        </div>
                        <h4>Виктория Зараменских</h4>
                        <h5>Web Designer</h5>
                    </div>
                </div>
                <div class="col-md-4 col-sm-6 col-xs-12 align-self-center">
                    <div class="card">
                        <div class="img-area">
                            <img src="../assets/img/team3.png" class="img-fluid" alt="Медиацентр">
                        </div>
                        <h4>Медиацентр МИЭМ</h4>
                        <h5>Заказчик</h5>
                    </div>
                </div>
                <div class="col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="img-area">
                            <img src="../assets/img/team2.png" class="img-fluid" alt="Попов">
                        </div>
                        <h4>Леонид Попов</h4>
                        <h5>Web Designer</h5>
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

export default {
    name: 'AboutPage',
    components: { MainHeader, MainFooter }
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