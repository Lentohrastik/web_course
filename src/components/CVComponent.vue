<template>
    <MainHeader />
    <section id="about" class="about">
        <div class="container p-4">
            <div class="row">
                <div class="col-lg-4 pt-4 pt-lg-0 content align-self-center">
                    <h3>Использование face recognition</h3>
                    <p class="fst-italic">
                        Face recognition - это передовая технология, которая позволяет автоматически распознавать и
                        идентифицировать
                        лицо человека на видеопотоке в реальном времени.
                    </p>
                </div>
                <div class="col-lg-4 pt-4 pt-lg-0 content">
                    <ul>
                        <li><i class="bi bi-check-circle"></i> Идентификация личности: Технология распознавания лиц
                            определяет, кто
                            находится перед камерой, и может сопоставить лицо с заранее вписанными данными о человеке.
                        </li>
                        <li><i class="bi bi-check-circle"></i> Зрительский опыт: Идентификация и предоставление
                            информации о
                            спикерах или участниках может улучшить пользовательский опыт и удовлетворенность аудитории.
                        </li>
                    </ul>
                </div>
                <div class="col-lg-4 my-auto">
                    <img src="../assets/img/cv.png" class="img-fluid " alt="face recognition">
                </div>
            </div>

        </div>
    </section>
    <MainFooter />
</template>

<script>


import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'CVPage',
    components: { MainHeader, MainFooter }
}
</script>


<style scoped>
/*---About---*/
.about .content h3 {
    font-weight: 600;
    font-size: 26px;
    color: #dad5d5;
}

.about .content ul {
    list-style: none;
    padding: 0;
}

.about .content ul li {
    padding-bottom: 10px;
}

.about .content ul i {
    font-size: 20px;
    padding-right: 4px;
    color: #463f65;
}

.about .content p:last-child {
    margin-bottom: 0;
}
</style>