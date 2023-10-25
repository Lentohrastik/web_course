<template>
    <MainHeader />

    <div class="container">
        <div class="row p-4 d-flex align-content-center">
            <div class="col-lg-2 col-md-3 col-sm-4 align-self-center">
                <img src="../assets/img/casparlogo.png" class="img-fluid">
            </div>
            <div class="col-lg-10 col-md-9 col-sm-8 text-center">
                <p>CasparCG Server - это программное обеспечение для Windows и Linux, используемое для воспроизведения
                    профессиональной графики, аудио и видео на несколько выходов. Он транслируется в режиме 24/7 с 2006
                    года.</p>
                <a href="https://casparcgforum.org" class="link-underline-primary link-opacity-25-hover">Перейти на
                    форум CasparCG<i class="bi bi-box-arrow-up-right"></i></a>
            </div>
        </div>
    </div>

    <MainFooter />
</template>
  
<script>
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'CasparPage',
    components: { MainHeader, MainFooter }
}
</script>