<template>
    <AppHeader />
    <main>
        <div class="container justify-content-center">
            <div class="pb-3 text-center text-white">
                <h2>Окно удаления спикеров</h2>
                <p class="mb-3">Выбирете спикера, которого хотите удалить, и нажмите на кнопку удалить рядом с его именем.
                </p>
                <div>
                    <p>Раскрыв выпадающий список можно посмотреть фотографию человека.</p>
                </div>
            </div>

            <div>
                <div v-for="(user, idx) in users" v-bind:key="idx" class="dropdown row p-4">
                    <div class="btn btn-secondary dropdown-toggle dropdown-toggle-split col" role="button"
                        id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                        {{ user.name }} -- {{ user.role }}
                    </div>

                    <div class="dropdown-menu col" aria-labelledby="dropdownMenuButton">
                        <img :src="user.src" class="img-fluid">
                    </div>
                    <div class="col" @click="delUser(idx)">
                        <a class="nav-link px-0 align-middle">
                            <i class="fs-4 text-white bi-dash-square"></i> <span
                                class="ms-1 d-none d-md-inline text-white "> Удалить </span></a>
                    </div>
                </div>
            </div>
        </div>

        <div v-show="isShow" class="alert alert-info text-center" role="alert">
            Пользователь успешно удалён!
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
    name: 'DelUserPage',
    components: { AppHeader, MainFooter },

    data() {
        return {
            users: [
                { name: "Попов Леонид", src: img1, role: "роль" },
                { name: "Виктория Зараменских", src: img2, role: "роль" },
                { name: "Иван Иванов", src: img3, role: "роль" },
                { name: "Андрей Иванов", src: img3, role: "роль" },
                { name: "Пётр Иванов", src: img3, role: "роль" },
            ],
            isShow: false,
        }
    },

    methods: {
        delUser(idx) {
            this.users.splice(idx, 1);
            this.isShow = true;
            setTimeout(() => {
                this.isShow = false;
            }, 5000)
        }
    }

}
</script>