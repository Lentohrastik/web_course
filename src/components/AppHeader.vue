<template>
    <header id="header" class="d-flex align-items-start">
        <div class="container-fluid justify-content-start align-items-center">

            <nav class="navbar navbar-expand-md bg-dark border-bottom border-body" data-bs-theme="dark">

                <div class="container-fluid">
                    <router-link class="navbar-brand" to="/">
                        <img src="../assets/logo.png" alt="logo" width="100">
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
                                <router-link to="/app" class="nav-link active">Назад</router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </header>
</template>

