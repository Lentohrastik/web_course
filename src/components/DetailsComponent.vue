<template>
    <MainHeader />

    <div class="container" id="details">
        <div class="row p-5 ps-0">
            <div class="col-6">
                <p>Титровальная система получает видео поток с камеры с помощью python кода, который запускается с
                    помощью телеграм бота, после распознавания лица информация о человеке отправляется в CasparCG для
                    создания титра и дальнейшей его отправки пользователю в виде ndi потока. Нейросеть, телеграм бот,
                    CasparCG находятся на сервере, что обеспечивает постоянную и автономную работу и простоту
                    использования пользователем системой</p>
            </div>
            <div class="col-6 justify-content-center align-content-center">
                <img src="../assets/img/lyonya.png" class="img-fluid" alt="lyonya">
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