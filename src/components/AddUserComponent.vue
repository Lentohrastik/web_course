<template>
    <AppHeader />
    <main>
        <div class="p-5">
            <div class="pb-3 text-center text-white">
                <h2>Окно добавления выступающих</h2>
                <p class="mb-3">Заполните информацию о человеке и загрузите его фото!</p>
                <div>
                    <p>Имя и роль должны быть написаны с большой буквы через пробел (<b>Пример: Иван Иванов</b>).</p>
                    <p>На фотографии должно быть строго одно лицо, иначе система не примит вашу фотографию.</p>
                </div>
            </div>

            <div class="card-group pb-5">
                <div v-for="(item, idx) in photoExaples" v-bind:key="idx" class="card">
                    <img :src="item.src" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="nav-link px-0">
                            <i class="fs-4 text-white" :class="item.class"></i> <span
                                class="ms-1 d-none d-md-inline text-white">{{ item.text }}</span>
                        </h5>
                    </div>
                </div>
                <!-- <div class="card">
                    <img src="../assets/img/carousel2.png" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="nav-link px-0">
                            <i class="fs-4 text-white bi-check-square"></i> <span
                                class="ms-1 d-none d-md-inline text-white">Один человек в кадре</span>
                        </h5>
                    </div>
                </div>
                <div class="card">
                    <img src="../assets/img/carousel4.png" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="nav-link px-0">
                            <i class="fs-4 text-white bi-dash-square"></i> <span
                                class="ms-1 d-none d-md-inline text-white">В кадре нет людей</span>
                        </h5>
                    </div>
                </div> -->
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
            image: "https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.png",
            photoExaples: [
                { class: "bi-dash-squar", text: "Несколько людей в кадре", src: "../assets/img/several_people.png" },
                { class: "bi-check-square", text: "Один человек в кадре", src: "../assets/img/one_people.png" },
                { class: "bi-dash-squar", text: "В кадре нет людей", src: "../assets/img/several_people.png" },
            ]
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