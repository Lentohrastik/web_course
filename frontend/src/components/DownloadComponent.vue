<template>
    <MainHeader />
    <!-- ======= Contact us ======= -->

    <div class="align-items-center justify-content-center p-5 pb-2">
        <h1 class="text-center">Свяжитесь с нами</h1>
        <p class="text-center">Для получения доступа к автоматической титровальной системе Вы можете оставить заявку, указав
            Ващи данные, и мы обязательно рассмотрим ее в ближайшее время.</p>
    </div>
    <div class="d-flex align-items-center justify-content-center mb-5">
        <form>
            <div class="mb-3 p-2" id="contactForm">
                <label for="inputEmail" class="form-label">Адрес электронной почты</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text">Мы никогда никому не передадим Ваши данные.</div>
            </div>
            <div class="mb-3 p-2" id="contactForm">
                <label for="inputName" class="form-label ">Имя и фамилия</label>
                <input type="text" class="form-control" id="inputName">
            </div>
            <div class="mb-3 p-2" id="contactForm">
                <label for="inputPhone" class="form-label">Номер телефона</label>
                <input type="tel" class="form-control" id="inputPhone">
            </div>
            <div class="text-center">
                <button type="submit" class="btn">Отправить</button>
            </div>

        </form>
    </div>
    <MainFooter />
</template>
    
<script>
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'DownloadPage',
    components: { MainHeader, MainFooter }
}
</script>

