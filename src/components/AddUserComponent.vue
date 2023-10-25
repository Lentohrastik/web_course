<template>
    <AppHeader />
    <main>
        <div class="p-5">
            <div class="pb-3 text-center text-white">
                <h2>Окно добавления выступающих</h2>
                <p>В данном окне можно добавлять пользователей для того, чтоб они распозновались!</p>
            </div>

            <div class="input-group mb-3">
                <span type="text" class="input-group-text" id="basic-addon1">Имя и Фамилия</span>
                <input type="text" class="form-control" placeholder="Имя Фамилия" aria-label="Имя Фамилия"
                    aria-describedby="basic-addon1">
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Роль</span>
                <input type="text" class="form-control" placeholder="Роль" aria-label="Роль"
                    aria-describedby="basic-addon1">
            </div>

            <div>
                <div class="d-flex justify-content-center mb-4">
                    <img :src="image" class="rounded-circle img-fluid" alt="example placeholder" style="width: 25em" />
                </div>

                <div class="d-flex justify-content-center center">
                    <div class="btn btn-primary btn-rounded">
                        <label class="form-label text-white m-1" for="customFile2">Выбирете фото</label>
                        <input type="file" id="customFile2" ref="myFiles" class="form-control d-none" @change="loadFile"
                            accept="image/*">
                    </div>
                </div>
            </div>

            <div class="p-5 d-flex justify-content-center center">
                <div class="btn btn-primary btn-rounded">
                    <i class="fs-4 bi-send-fill text-white"></i>
                    <span class="ms-1 d-none d-sm-inline text-white">
                        <label class="form-label text-white m-1">Отправить</label>
                    </span>

                </div>
            </div>
        </div>
    </main>
    <MainFooter />
</template>
  
<script>
import AppHeader from './AppHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'AddUserPage',
    components: { AppHeader, MainFooter },

    data() {
        return {
            image: "https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.png"
        };
    },

    methods: {
        loadFile(e) {
            const file = e.target.files[0];
            this.image = URL.createObjectURL(file)
        }
    }
}
</script>