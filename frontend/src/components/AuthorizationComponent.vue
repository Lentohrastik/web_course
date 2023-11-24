<template>
    <MainHeader />
    <main>
        <section class="vh-100">
            <div class="container-fluid h-custom">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-md-9 col-lg-6 col-xl-5">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
                            class="img-fluid" alt="Sample image">
                    </div>

                    <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
                        <div v-show="isShowNotification" class="alert alert-danger text-center" role="alert">
                            {{ notificationText }}
                        </div>
                        <h7 v-show="isForgot" class="text-center">Введите подтвержденный адрес электронной почты вашей
                            учетной записи пользователя, и мы вышлем вам ссылку для сброса пароля</h7>
                        <form class="p-3">
                            <!-- Email input -->
                            <div v-show="isReg || isLogin || isForgot" class="form-outline mb-4">
                                <input v-model="email" type="email" id="form3Example3" class="form-control form-control-lg"
                                    placeholder="Email" />
                                <label class="form-label" for="form3Example3">Адрес электронной почты</label>
                            </div>

                            <!-- Username input -->
                            <div v-show="isReg" class="form-outline mb-4">
                                <input v-model="username" type="text" class="form-control form-control-lg"
                                    placeholder="Username" />
                                <label class="form-label">Имя пользователя</label>
                            </div>

                            <!-- Password input -->
                            <div v-show="isReg || isLogin" class="form-outline mb-3">
                                <input v-model="password" type="password" id="form3Example4"
                                    class="form-control form-control-lg" placeholder="Пароль" />
                                <label class="form-label" for="form3Example4">Пароль</label>
                            </div>

                            <div v-show="isLogin" class="d-flex justify-content-between align-items-center">
                                <!-- Checkbox -->
                                <div class="form-check mb-0">
                                    <label class="form-check-label" for="form2Example3">
                                    </label>
                                </div>
                                <a v-show="isLogin" class="href" @click="forgotPassword">Забыли пароль?</a>
                            </div>

                            <div v-show="isReg || isLogin || isForgot" class="text-center text-lg-start mt-4 pt-2">
                                <button @click="clickButton" type="button" class="btn btn-primary btn-lg"
                                    style="padding-left: 2.5rem; padding-right: 2.5rem;">{{ buttonText }}</button>
                                <p class="small fw-bold mt-2 pt-1 mb-0">{{ accountText }} <a class="href"
                                        @click="checkOut">{{
                                            checkOutText
                                        }}</a></p>
                            </div>

                            <!-- Reset password-->
                            <h7 v-show="isSetNewPassword" class="text-center">Введите токен, который вы получили на почту и
                                новый пароль</h7>
                            <!-- token input -->
                            <div v-show="isSetNewPassword" class="form-outline mb-4">
                                <input v-model="token" type="text" class="form-control form-control-lg"
                                    placeholder="Token" />
                                <label class="form-label">Token</label>
                            </div>

                            <!-- New Password input -->
                            <div v-show="isSetNewPassword" class="form-outline mb-3">
                                <input v-model="newPassword" type="password" id="form3Example4"
                                    class="form-control form-control-lg" placeholder="Новый пароль" />
                                <label class="form-label" for="form3Example4">Новый пароль</label>
                            </div>

                            <div v-show="isSetNewPassword" class="text-center text-lg-start mt-4 pt-2">
                                <button @click="setNewPassword" type="button" class="btn btn-primary btn-lg"
                                    style="padding-left: 2.5rem; padding-right: 2.5rem;">Сменить пароль</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <MainFooter />
</template>
  
<script>
import axios from 'axios';
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'AuthorizationPage',
    components: { MainHeader, MainFooter },
    data() {
        return {
            email: '',
            password: '',
            username: '',
            newPassword: '',
            token: '',
            isShowNotification: false,
            notificationText: '',
            buttonText: 'Войти',
            accountText: 'Нет аккаунта?',
            checkOutText: 'Зарегестрироваться',
            isReg: false,
            isLogin: true,
            isForgot: false,
            isSetNewPassword: false,
        }
    },
    methods: {
        login() {
            var body = {
                username: this.email,
                password: this.password,
            }

            axios({
                method: 'post',
                url: 'http://localhost:4446/auth/login',
                data: body,
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                withCredentials: true,
            })
                .then(() => {
                    this.$router.push('/app')
                })
                .catch(() => {
                    this.notificationText = 'Неверный логин или пароль!';
                    this.isShowNotification = true;
                    setTimeout(() => {
                        this.isShowNotification = false;
                    }, 5000)
                });

        },

        registr() {
            var body = {
                email: this.email,
                username: this.username,
                password: this.password,
            }

            axios({
                method: 'post',
                url: 'http://localhost:4446/auth/register',
                data: body,
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    this.login();
                })
                .catch((error) => {
                    this.isShowNotification = true;
                    if (error.response.data.detail == 'REGISTER_USER_ALREADY_EXISTS') {
                        this.notificationText = 'Данный пользователь уже существует!';
                    } else {
                        this.notificationText = 'Пароль должен быть больше 3 символов!';
                    }
                    setTimeout(() => {
                        this.isShowNotification = false;
                    }, 5000)
                });
        },

        forgot() {
            var body = {
                email: this.email,
            }

            axios({
                method: 'post',
                url: 'http://localhost:4446/auth/forgot-password',
                data: body,
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    this.isForgot = false;
                    this.isSetNewPassword = true;
                })
                .catch(() => {
                    this.isShowNotification = true;
                    this.notificationText = 'Что-то пошло не так! Повторите попытку позже!';
                    setTimeout(() => {
                        this.isShowNotification = false;
                    }, 5000)
                });
        },

        clickButton() {
            if (this.isLogin) {
                this.login();
            } else if (this.isReg) {
                this.registr();
            } else {
                this.forgot();
            }
        },

        forgotPassword() {
            this.isLogin = false;
            this.isReg = false;
            this.isForgot = true;
            this.buttonText = 'Отправить';
            this.accountText = 'Вспомнили пароль?';
            this.checkOutText = 'Войти';
        },

        checkOut() {
            if (this.isLogin) {
                this.buttonText = 'Зарегестрироваться';
                this.accountText = 'Есть аккаунт?';
                this.checkOutText = 'Войти';
                this.isLogin = false;
                this.isReg = true;
            } else {
                this.buttonText = 'Войти';
                this.accountText = 'Нет аккаунта?';
                this.checkOutText = 'Зарегестрироваться';
                this.isReg = false;
                this.isForgot = false;
                this.isLogin = true;
            }
        },

        setNewPassword() {
            var body = {
                token: this.token,
                password: this.newPassword,
            }

            axios({
                method: 'post',
                url: 'http://localhost:4446/auth/reset-password',
                data: body,
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            })
                .then(() => {
                    this.isLogin = true;
                    this.isSetNewPassword = false;
                    this.buttonText = 'Войти';
                    this.accountText = 'Нет аккаунта?';
                    this.checkOutText = 'Зарегестрироваться';
                    this.isShowNotification = true;
                    this.notificationText = 'Вы сменили пароль';
                    setTimeout(() => {
                        this.isShowNotification = false;
                    }, 5000)
                })
                .catch((error) => {
                    this.isShowNotification = true;
                    if (error.response.data.detail == 'RESET_PASSWORD_BAD_TOKEN') {
                        this.notificationText = 'Токен истёк или неверен!';
                    } else {
                        this.notificationText = 'Пароль должен быть больше 3 символов!';
                    }
                    setTimeout(() => {
                        this.isShowNotification = false;
                    }, 5000)
                });
        }
    }
}
</script>

<style scoped>
.divider:after,
.divider:before {
    content: "";
    flex: 1;
    height: 1px;
    background: #eee;
}

.h-custom {
    height: calc(100% - 73px);
}

@media (max-width: 450px) {
    .h-custom {
        height: 100%;
    }
}
</style>