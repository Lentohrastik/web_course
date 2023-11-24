<template>
    <MainAppHeader />
    <main>
        <div class="container-fluid">
            <div class="row flex">
                <div class="col-md-3 col-1 px-sm-2 px-0 bg-dark">
                    <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-200"
                        id="menu_dev">
                        <a class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                            <span class="fs-5 d-none d-sm-inline">Возможности</span>
                        </a>
                        <ul v-for="(item, idx) in this.navigationMenuList" v-bind:key="idx"
                            class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
                            id="menu">
                            <li>
                                <a @click="gotToPage(item.href)" href="#start_rec" class="nav-link px-0 align-middle">
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
        <div id="start_rec">
            <div v-show="isShowRec" class="p-5">
                <p class="text-center">Введите RTSP поток и нажмите Entr!</p>
                <div class="input-group mb-3">
                    <span type="text" class="input-group-text">RTSP поток</span>
                    <input v-on:keyup.enter="setRtsp" v-model="rtsp" type="text" class="form-control"
                        placeholder="RTSP поток" aria-label="RTSP поток" aria-describedby="basic-addon1">
                </div>
            </div>
            <div v-show="isShow" class="alert alert-info text-center" role="alert">
                {{ notification }}
            </div>
        </div>
    </main>
    <MainFooter />
</template>
  
<script>
import MainFooter from './MainFooter.vue';
import MainAppHeader from './MainAppHeader.vue';

export default {
    name: 'AppPage',
    components: { MainAppHeader, MainFooter },

    data() {
        return {
            navigationMenuList: [
                { href: "/app/add_user", text: "Добавить пользователя", class: "bi-person-add" },
                { href: "/app/del_user", text: "Удалить пользователя", class: "bi-person-dash" },
                { href: "/app/template", text: "Выбрать шаблон", class: "bi-table" },
                { href: "/app/obs", text: "Настроить OBS config", class: "bi-camera-reels" },
                { href: "start", text: "Начать распознавание", class: "bi-search" },
                { href: "stop", text: "Закончить распознавание", class: "bi-stop-btn" },
            ],

            mainTextList: [
                { btn: "Добавить пользователя", info: " - данная кнопка предназначена для загрузки фотографии, имени и роли человека в базу данных вашей команды. Обязательно добавьте хотя бы одного человека, иначе распознование не запустится." },
                { btn: "Удалить пользователя", info: " -  данная кнопка предназначена для удаления фотографии, имени и роли человека из базы данных вашей команды. Будьте внимательны: после удаления восстановить фотографию будет невозможно." },
                { btn: "Выбрать шаблон", info: " - данная кнопка предназначена для выбора шаблона титра, который будет использоваться во время эфира. Пока на выбор предлагается всего 3 варианта титра, но скоро появятся ещё." },
                { btn: "Настроить OBS config", info: " - данная кнопка предназначена для добавления информации об IP адресе, порте и пароле от программы OBS, на которой производится запись." },
                { btn: "Начать распознавание", info: " - данная кнопка предназначена для начала процесса распознавания, в процессе которого программа принимает RTSP поток с камеры и сравнивает изображения из потока с имеющимеся." },
                { btn: "Закончить распознавание", info: " - данная кнопка предназначена для остановки процесса распознавания." },
            ],
            isShow: false,
            isShowRec: false,
            rtsp: "",
            notification: "",
        };
    },

    methods: {
        showNot() {
            setTimeout(() => {
                this.isShow = false;
            }, 5000)
        },

        gotToPage(path) {
            if (path == "stop") {
                this.notification = "Распознавание успешно завершено!"
                this.isShow = true;
                this.showNot();
            } else if (path == "start") {
                this.notification = "Распознавание началось!"
                this.isShowRec = true;
                this.rtsp = "";
            } else {
                this.$router.push(path);
            }
        },
        setRtsp() {
            this.isShow = true;
            this.showNot();
            setTimeout(() => {
                this.isShowRec = false;
            }, 2000)

        }
    }
}
</script>