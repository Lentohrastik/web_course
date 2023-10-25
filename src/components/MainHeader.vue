<template>
    <header id="header" class="d-flex align-items-start">
        <div class="container-fluid justify-content-start align-items-center">

            <!-- Navbar -->
            <nav class="navbar navbar-expand-md bg-dark border-bottom border-body" data-bs-theme="dark">

                <div class="container-fluid">
                    <router-link class="navbar-brand" to="/">
                        <img src="../assets/logo.svg" alt="logo" width="60">
                        Auto Caption System</router-link>
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
                            <router-link id="butt" to="/app" class="btn btn">Войти в ACS</router-link>
                        </div>
                    </div>

                </div>
            </nav>
        </div>
    </header>
</template>


<style>
.btn {
    background-color: #6897C9;
    color: #FFFAFF;
}

.btn:hover {
    background-color: #15171a;
    color: #6897C9;
    border-color: #6897C9;
}
</style>