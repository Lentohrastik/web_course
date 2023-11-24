<template>
  <!-- Carousel -->
  <div id="carouselIndicators" class="carousel carousel-dark slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselIndicators" data-bs-slide-to="0" class="active" aria-current="true"
        aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">

      <div v-for="(item, idx) in carouselList" v-bind:key="idx" :class="item.class" class="carousel-item"
        :style="{ 'background-image': 'url(' + item.url + ')' }">
        <div class="carousel-container p-2">
          <div class="carousel-content">
            <h3>{{ item.h3 }}</h3>
            <p>{{ item.p }}</p>
          </div>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselIndicators" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Предыдущий</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselIndicators" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Следующий</span>
    </button>
  </div>
</template>

<script>
import img1 from "../assets/img/carousel1.png";
import img2 from "../assets/img/carousel2.png";
import img3 from "../assets/img/carousel4.png";

export default {

  data() {
    return {
      carouselList: [
        { class: "active", url: img1, h3: "Уникальная технология", p: "Автоматическая титровальная система - узкоспециализированная программа для распознавания спикеров в прямом эфире" },
        { class: "", url: img2, h3: "Четкость и быстрота", p: "Больше не нужно запоминать спикеров.\nДостаточно сфотографировать спикеров и запустить программу" },
        { class: "", url: img3, h3: "Титры на любой вкус", p: "Используйте шаблоны из широкого списка представленных" },
      ]
    }
  }
}
</script>

<style scoped>
/* --Carousel--*/
#carouselIndicators {

  .carousel-control-next,
  .carousel-control-prev {
    filter: invert(100%);
  }

  .carousel-indicators {
    filter: invert(100%);
  }

  .carousel {
    margin-bottom: 50px;
  }

  .carousel-item {
    width: 100%;
    height: 100vh;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-position: center center;
  }

  .carousel-container {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
  }

  .carousel-content {
    text-align: center;
  }

  h3 {
    margin-bottom: 30px;
    font-size: 50px;
    font-weight: 600;
  }

  p {
    margin: 0 auto 30px auto;
    font-size: 24px;
    font-weight: 700;
  }
}

@media (max-height: 769px) {
  #carouselIndicators h3 {
    margin-bottom: 30px;
    font-size: 40px;
    font-weight: 500;
  }

  #carouselIndicators p {
    font-size: 20px;
    font-weight: 300;
  }

}
</style>