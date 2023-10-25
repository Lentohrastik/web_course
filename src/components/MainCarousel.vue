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
      <div class="carousel-item active"
        :style="{ 'background-image': 'url(' + require('../assets/img/carousel1.png') + ')' }">
        <div class="carousel-container p-2">
          <div class="carousel-content">
            <h3>Уникальная технология</h3>
            <p>Автоматическая титровальная система - узкоспециализированная программа для распознавания спикеров в
              прямом эфире</p>
          </div>
        </div>
      </div>
      <div class="carousel-item" :style="{ 'background-image': 'url(' + require('../assets/img/carousel2.png') + ')' }">
        <div class="carousel-container p-2">
          <div class="carousel-content">
            <h3>Четкость и быстрота</h3>
            <p>Больше не нужно запоминать спикеров.</p>
            <p>Достаточно сфотографировать спикеров и запустить программу</p>
          </div>
        </div>
      </div>

      <div class="carousel-item" :style="{ 'background-image': 'url(' + require('../assets/img/carousel4.png') + ')' }">
        <div class="carousel-container p-2">
          <div class="carousel-content">
            <h3>Титры на любой вкус</h3>
            <p>Используйте шаблоны из широкого списка представленных</p>
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
export default {
  data() {
    return {
    }
  }
}
</script>

<style scoped>
/* --Carousel--*/
#carouselIndicators {
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
  #carouselIndicators {
    height: 70vh;
  }

  #carouselIndicators .carousel-item {
    height: 70vh;
  }

  #carouselIndicators h3 {
    margin-bottom: 30px;
    font-size: 40px;
    font-weight: 500;
  }

  #carouselIndicators p {
    font-size: 20px;
    font-weight: 300;
  }

}</style>