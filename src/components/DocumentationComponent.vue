<template>
    <MainHeader />

    <!--    Scrollspy   -->
    <div class="row flex-nowrap" id="scrollspy">
        <div id="scrollspy-nav" class="col-auto col-md-4 col-xl-3 px-sm-2 px-0 bg-dark d-none d-md-block">
            <nav class="navbar navbar-dark bg-dark flex-column align-items-stretch p-3"></nav>
            <nav class="nav nav-pills flex-column">
                <a class="nav-link" href="#item-1">Запуск кода. OBS</a>
                <nav class="nav nav-pills flex-column">
                    <a class="nav-link ms-3 my-1" href="#item-1-1">Сцена с detected_name</a>
                    <a class="nav-link ms-3 my-1" href="#item-1-2">Выбор NDI ресурса</a>
                </nav>
                <a class="nav-link" href="#item-2">Запуск нейросети</a>
                <a class="nav-link" href="#item-3">Telegram bot</a>
                <nav class="nav nav-pills flex-column">
                    <a class="nav-link ms-3 my-1" href="#item-3-1">Информация о человеке</a>
                    <a class="nav-link ms-3 my-1" href="#item-3-2">Запуск распознавания</a>
                </nav>
            </nav>
        </div>
        <div class="col-sm-12 col-md-8 p-5" id="scrollspy-content">
            <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-offset="0" tabindex="0">
                <h4 id="item-1">Запуск кода. OBS</h4>
                <p>Открыть OBS версии 28+ и
                    включить в Tools WebSocket Server Settings с помощью галочки Enable WebSocket Server
                    Settings.</p>
                <h5 id="item-1-1">Сцена с detected_name</h5>
                <p>Необходимо, чтобы был на сцене
                    текстовый сурс с названием detected_name. При необходимости нужно настроить размеры
                    текста, чтобы был корректно виден.</p>
                <h5 id="item-1-2">Выбор NDI ресурса</h5>
                <p>На сцене, где будет выводиться
                    титр необходимо создать NDI Source, где в Source Name указать поток с названием в
                    скобках CasparCG_1 (например: ASSISTANT-PC (CasparCG_1); добавить фильтр с
                    хромакеем
                </p>
                <h4 id="item-2">Запуск нейросети</h4>
                <p>Запустить файл
                    auto-caption.exe. Должен открыться каспар и два окна Командной строки (В них можно
                    посмотреть ошибки, в основном нужно для мониторинга).</p>
                <p>Чтобы запустить на данный
                    момент титр при распознании человека, нужно запустить insomnia с сайтом
                    127.0.0.1:4446/send_ndi (для запуска титра заново - нажать кнопку send)
                </p>
                <h4 id="item-3">Telegram bot</h4>
                <p>Чтобы начать работу с телеграм ботом (@auto_titration_bot) необходимо ввести команду /start и
                    ввести пароль, который можно задать в config файле. После ввода пароля он удалится из переписки.
                    При неправильном вводе пароля бот напишет сообщение &ldquo;В доступе отказано!&rdquo;.</p>
                <h5 id="item-3-1">Информация о человеке</h5>
                <p>При нажатии на кнопку &ldquo;Редактировать инф-цию о человеке" выведется список людей и после
                    выбора&nbsp; меню с выбором, что нужно отредактировать.</p>
                <h5 id="item-3-2">Запуск распознавания</h5>
                <p>Для того, чтобы распознать человека во время съемки, необходимо после всей настройки нажать на
                    кнопку "Начать распознавание", после чего бот вышлет сообщение с запросом rtsp пути камеры, с
                    которой нужно распознавать.</p>

            </div>
        </div>
    </div>

    <MainFooter />
</template>


<script>
import MainHeader from './MainHeader.vue';
import MainFooter from './MainFooter.vue';

export default {
    name: 'DocumentationPage',
    components: { MainHeader, MainFooter }
}
</script>