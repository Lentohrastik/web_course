<template>
    <AppHeader />
    <main>
        <div class="pb-3 text-center text-white">
            <h2>Окно Выбора шаблона</h2>
            <p>В данном окне можно выброть понравившийся шаблон!</p>
        </div>

        <div class="container text-center">
            <div class="row p-5 d-flex">
                <div class="col-6">
                    <img src="../assets/img/pic01.png" class="img-fluid" alt="template 1">
                </div>
                <div class="form-check col-6 align-self-center">
                    <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                    <label class="form-check-label" for="flexRadioDefault1">
                        Шаблон 1
                    </label>
                </div>
            </div>

            <div class="row p-5 d-flex">
                <div class="col-6">
                    <img src="../assets/img/pic02.png" class="img-fluid" alt="template 2">
                </div>
                <div class="form-check col-6 align-self-center">
                    <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                    <label class="form-check-label" for="flexRadioDefault1">
                        Шаблон 2
                    </label>
                </div>
            </div>

            <div class="row p-5 d-flex ">
                <div class="col-6 ">
                    <img src="../assets/img/pic03.png" class="img-fluid" alt="template 3">
                </div>
                <div class="form-check col-6 align-self-center">
                    <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                    <label class="form-check-label" for="flexRadioDefault1">
                        Шаблон 3
                    </label>
                </div>
            </div>
        </div>

        <div class="p-5 d-flex justify-content-center">
            <div class="btn btn-primary btn-rounded">
                <i class="fs-4 bi-send-fill text-white"></i>
                <span class="ms-1 d-none d-sm-inline text-white">
                    <label class="form-label text-white m-1">Отправить</label>
                </span>
            </div>
        </div>
    </main>
    <MainFooter />
</template>
  
<script>
import AppHeader from './AppHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'TemplatePage',
    components: { AppHeader, MainFooter }
}
</script>