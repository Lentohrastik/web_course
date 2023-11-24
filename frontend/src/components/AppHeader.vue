<template>
    <header id="header" class="d-flex align-items-start">
        <div class="container-fluid justify-content-start align-items-center">

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
                        <ul v-for="(item, idx) in navList" v-bind:key="idx" class="navbar-nav">
                            <li class="nav-item">
                                <router-link :to="item.to" class="nav-link active">{{ item.text }}</router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </header>
</template>

<script>
export default {
    data() {
        return {
            navList: [
                { to: "/", text: "Главная" },
                { to: "/app", text: "Назад" },
            ]
        };
    }
}
</script>

