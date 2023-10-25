<template>
    <MainHeader />
    <main>
        <div class="container-fluid">
            <div class="row flex-nowrap">
                <div class="col-md-4 col-xl-3 px-sm-2 px-0 bg-dark">
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
                                    <i class="fs-4 bi-table text-white"></i> <span
                                        class="ms-1 d-none d-sm-inline text-white"> {{ item.text }} </span></a>
                            </li>
                        </ul>
                        <hr>
                    </div>
                </div>
                <div class="col py-3">
                    <p v-for="(item, idx) in mainTextList" v-bind:key="idx" class="plain_text"><b>{{ item.btn }}</b>{{
                        item.info }}</p>
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
                { href: "/app/add_user", text: "Добавить пользователя" },
                { href: "#", text: "Удалить пользователя" },
                { href: "/app/template", text: "Выбрать шаблон" },
                { href: "/app/obs", text: "Настроить OBS config" },
                { href: "#", text: "Вывести человека с фото" },
                { href: "#", text: "Начать распознавание" },
                { href: "#", text: "Закончить распознавание" },
            ],

            mainTextList: [
                { btn: "Добавить пользователя", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
                { btn: "Удалить пользователя", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
                { btn: "Выбрать шаблон", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
                { btn: "Настроить OBS config", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
                { btn: "Вывести человека с фото", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
                { btn: "Начать распознавание", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
                { btn: "Закончить распознавание", info: " - кнопка для добавления информации о пользоватеея в базу данных" },
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