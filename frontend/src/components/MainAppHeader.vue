<template>
    <header id="header" class="d-flex align-items-start">
        <div class="container-fluid justify-content-start align-items-center">

            <!-- Navbar -->
            <nav class="navbar navbar-expand-md bg-dark border-bottom border-body" data-bs-theme="dark">

                <div class="container-fluid">
                    <router-link class="navbar-brand" to="/">
                        <atropos-component class="my-atropos">
                            <img src="../assets/logo.svg" alt="logo" width="60" data-atropos-offset="5">
                        </atropos-component>
                    </router-link>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <router-link to="/" class="nav-link active">Главная</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link to="/download" class="nav-link">Скачать</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link to="/documentation" class="nav-link">Документация</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link to="/charts" class="nav-link">Графики</router-link>
                            </li>
                            <!-- Dropdown -->
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" data-bs-auto-close="outside" href="#" role="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    Что это?
                                </a>
                                <ul class="dropdown-menu">

                                    <li>
                                        <router-link to="/details" class="dropdown-item">Подробнее о системе
                                            титрования</router-link>
                                    </li>
                                    <li>
                                        <router-link to="/learn" class="dropdown-item">Обучающие видео</router-link>
                                    </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                    <!-- Dropdown -->
                                    <li class="dropend">
                                        <a class="dropdown-item dropdown-toggle" href="#" role="button"
                                            data-bs-toggle="dropdown">Используемые технологии</a>
                                        <ul class="dropdown-menu">
                                            <li><router-link to="/casparcg" class="dropdown-item">CasparCG</router-link>
                                            </li>
                                            <router-link to="/cv" class="dropdown-item">Computer Vision</router-link>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="nav-item">
                                <router-link to="/about" class="nav-link">О нас</router-link>
                            </li>
                        </ul>
                        <div class="ms-lg-auto text-center">
                            <div @click="logout" id="butt" class="btn btn">Выйти из ACS</div>
                        </div>
                    </div>

                </div>
            </nav>
        </div>
    </header>
</template>

<script>
import axios from 'axios';
export default {
    methods: {
        logout() {
            axios({
                method: 'post',
                url: 'http://localhost:4446/auth/logout',
                headers: {
                    'accept': 'application/json'
                },
                withCredentials: true,
            })
                .then(() => {
                    this.$router.push('/')
                })
                .catch(() => {
                    this.notificationText = 'Что-то пошло не так!';
                    this.isShowNotification = true;
                    setTimeout(() => {
                        this.isShowNotification = false;
                    }, 5000)
                });
        }
    }
}
</script>