<template>
    <MainHeader />
    <main>
        <div class="container-fluid">
            <div class="row flex">
                <div class="col-md-3 col-1 px-sm-2 px-0 bg-dark">
                    <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-200"
                        id="menu_dev">
                        <a class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                            <span class="fs-5 d-none d-sm-inline">Menu</span>
                        </a>
                        <ul v-for="(item, idx) in this.navigationMenuList" v-bind:key="idx"
                            class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
                            id="menu">
                            <li>
                                <a @click="gotToPage(item.href)" class="nav-link px-0 align-middle">
                                    <i :class="item.class" class="fs-4 text-white"></i> <span
                                        class="ms-1 d-none d-md-inline text-white "> {{ item.text }} </span></a>
                            </li>
                        </ul>
                        <hr>
                    </div>
                </div>
                <div class="col  py-5">
                    <h4 class="plain_text text-center">Auto caption system</h4>
                    <p class="plain_text text-center">В данном разделе можно прочитать описание всех возможностей системы
                        автоматического титрования и перейти к интересующему вас разделу.</p>
                    <hr>
                    <p v-for="(item, idx) in mainTextList" v-bind:key="idx" class="plain_text"><b>{{ item.btn }}</b>{{
                        item.info }}</p>
                    <hr>
                </div>
            </div>
        </div>
    </main>
    <MainFooter />
</template>
  
<script>
import MainFooter from './MainFooter.vue';
import MainHeader from './MainHeader.vue';

export default {
    name: 'AppPage',
    components: { MainHeader, MainFooter },

    data() {
        return {
            navigationMenuList: [
                { href: "/app/add_user", text: "Добавить пользователя", class: "bi-person-add" },
                { href: "#", text: "Удалить пользователя", class: "bi-person-dash" },
                { href: "/app/template", text: "Выбрать шаблон", class: "bi-table" },
                { href: "/app/obs", text: "Настроить OBS config", class: "bi-camera-reels" },
                { href: "#", text: "Вывести человека с фото", class: " bi-file-earmark-person" },
                { href: "#", text: "Начать распознавание", class: "bi-search" },
                { href: "#", text: "Закончить распознавание", class: "bi-stop-btn" },
            ],

            mainTextList: [
                { btn: "Добавить пользователя", info: " - данная кнопка предназначена для загрузки фотографии, имени и роли человека в базу данных вашей команды. Обязательно добавьте хотя бы одного человека, иначе распознование не запустится." },
                { btn: "Удалить пользователя", info: " -  данная кнопка предназначена для удаления фотографии, имени и роли человека из базы данных вашей команды. Будьте внимательны: после удаления восстановить фотографию будет невозможно." },
                { btn: "Выбрать шаблон", info: " - данная кнопка предназначена для выбора шаблона титра, который будет использоваться во время эфира. Пока на выбор предлагается всего 3 варианта титра, но скоро появятся ещё." },
                { btn: "Настроить OBS config", info: " - данная кнопка предназначена для добавления информации об IP адресе, порте и пароле от программы OBS, на которой производится запись." },
                { btn: "Вывести человека с фото", info: " - данная кнопка предназначена для того, чтобы посмотреть фотографию, имя, роль человека, добавленного в базу данных вашей команды." },
                { btn: "Начать распознавание", info: " - данная кнопка предназначена для начала процесса распознавания, в процессе которого программа принимает RTSP поток с камеры и сравнивает изображения из потока с имеющимеся." },
                { btn: "Закончить распознавание", info: " - данная кнопка предназначена для остановки процесса распознавания." },
            ]
        };
    },

    methods: {
        gotToPage(path) {
            this.$router.push(path);
        }
    }
}
</script>