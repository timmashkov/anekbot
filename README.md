Моя мама любит анекдоты и сидеть в телеграмме, поэтому для нее я написал бота, который тянет анекдоты с сайта anekdots.ru 
Так как никакого функционала кроме анекдотов не предполагалось, я выбрал библиотеку telebot, простую но функциональную.
С сайта anekdot.ru парсится страница с самими анекдотами и превращается в список строк, которые рандомно перемешиваются
и передаются непосредственно боту. Однажды использованная строка удаляется из списка. По кнопке старт и фразе 
'хочу смеяться 5 минут' (независимо от регистра) бот возврашает анекдот.
![2023-07-02_13-31-37](https://github.com/timmashkov/anekbot/assets/106866033/d134c263-b290-425b-8f04-7979ac13cc16)