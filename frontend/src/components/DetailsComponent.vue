<template>
    <MainHeader />

    <div class="container m-3 align-item-center" id="details">
        <div class="row  p-5">
            <div class="col-12 col-md-6 align-self-center">
                <p>Титровальная система получает видео поток с камеры с помощью python кода, который запускается с
                    помощью телеграм бота, после распознавания лица информация о человеке отправляется в CasparCG для
                    создания титра и дальнейшей его отправки пользователю в виде ndi потока. Нейросеть, телеграм бот,
                    CasparCG находятся на сервере, что обеспечивает постоянную и автономную работу и простоту
                    использования пользователем системой</p>
            </div>
            <div class="col-12 col-md-6 justify-content-center align-self-center">
                <img src="../assets/img/lyonya.png" class="img-fluid" alt="lyonya">
            </div>
        </div>

        <div class="row p-5">
            <div class="col-12 col-md-6 justify-content-center align-self-center">
                <img src="../assets/img/obs.png" class="img-fluid" alt="lyonya">
            </div>
            <div class="col-12 col-md-6 align-self-center">
                <p>На данный момент вывод титра происходит в OBS. Для того, чтобы его настроить перейдите в приложение и в
                    настройки OBS.</p>
                <p>Для более подробной информации читайте документацию. </p>
            </div>
        </div>
    </div>
    <MainFooter />
</template>
  
<script>
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'DetailsPage',
    components: { MainHeader, MainFooter }
}
</script>