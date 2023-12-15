<template>
    <AppHeader />
    <main>
        <div class="p-5">
            <div class="pb-3 text-center text-white">
                <h2>Окно настройки OBS конфига</h2>
                <p>В данном окне можно настроить подключение к вашей локальной OBS! Порт, IP адрес и пароль можно найти в
                    настройках OBS websocket!</p>
            </div>

            <div class="input-group mb-3">
                <span type="text" class="input-group-text" id="basic-addon1">IP адрес OBS</span>
                <input v-model="obsHost" type="text" class="form-control" placeholder="Введите IP адрес OBS"
                    aria-label="IP адрес OBS" aria-describedby="basic-addon1">
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Порт OBS</span>
                <input v-model="obsPort" type="text" class="form-control" placeholder="Введите порт OBS"
                    aria-label="Введите порт OBS" aria-describedby="basic-addon1">
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Парль от OBS</span>
                <input v-model="obsPass" type="text" class="form-control" placeholder="Введите пароль"
                    aria-label="Введите пароль" aria-describedby="basic-addon1">
            </div>

            <div class="p-5 d-flex justify-content-center center">
                <div class="btn btn-primary btn-rounded" @click="send">
                    <i class="fs-4 bi-send-fill text-white"></i>
                    <span class="ms-1 d-none d-sm-inline text-white">
                        <label class="form-label text-white m-1">Отправить</label>
                    </span>
                </div>
            </div>
        </div>
        <div v-show="isShowNotification" class="alert alert-info text-center" role="alert">
            {{ notificationText }}
        </div>
    </main>
    <MainFooter />
</template>
  
<script>
import axios from 'axios';
import AppHeader from './AppHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'OBSPage',
    components: { AppHeader, MainFooter },
    data() {
        return {
            notificationText: '',
            isShowNotification: false,
            obsHost: '',
            obsPort: '',
            obsPass: ''
        }
    },

    methods: {
        showNotification(text) {
            this.notificationText = text;
            this.isShowNotification = true;
            setTimeout(() => {
                this.isShowNotification = false;
            }, 5000)
        },

        send() {
            var body = {
                "obs_host": this.obsHost,
                "obs_port": +this.obsPort,
                "obs_password": this.obsPass
            }

            console.log(body)

            axios({
                method: 'patch',
                url: 'http://localhost:4446/users/me',
                data: body,
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                withCredentials: true
            })
                .then(() => {
                    this.showNotification('Оbs конфиг записан!')
                })
                .catch((error) => {
                    console.log(error)
                    this.showNotification('Что-то пошло не так!')
                });
        }
    }
}
</script>