<template>
    <MainHeader />
    <MainCarousel />
    <MainFooter />
</template>
  
<script>
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';
import MainCarousel from './MainCarousel.vue';

export default {
    name: 'HomePage',
    components: { MainHeader, MainFooter, MainCarousel }
}
</script>