# parsing_KINOPOISK

**Задача:** построить парсер, принимающий уникальный идентификатор пользователя Кинопоиска, возвращающий информацию об оценках фильмов этим пользователем.

**Обоснование:** в будущем, горизонтально расширяя такой парсер смогли бы в перспективе построить улучшенную версию рекомендательной системы фильмов, которая будет основываться на множестве разных сервисов-социальных сетей для любителей кино и сериалов.

*Инструкция по сборке и запуску кода:*

Открыть файл parsing_KINOPOISK(HW_23.2.1).py в IDE. Перед запуском программы может потребоваться внести в окружение новые модули. В программе используются следующие модули: requests pandas openpyxl beautifulsoup4 lxml При вызове функции "collect_user_rates()" необходимо в значение переменной "user_login" внести идетификатор пользователя, данные которого нужно получить следующим образом: Выбрав конкретного пользователя, перейдите в его профиль. В адресной строке индетификатор пользователя будет выглядеть так: https://www.kinopoisk.ru/user/**77483303**/ По умолчанию значение установлено 77483303. Запустить код программы, кнопкой run в IDE. Отправленные URI будут выведена на печать в консоль. Полученные данные будут записаны в файл "user_rates.xlsx".

**ВНИМАНИЕ!!! Из-за защиты сайта Кинопоиск от парсинга, может потребоваться несколько запусков программы, так как она может не находить данных на сайте. (Иногда программа может найти только несколько страниц)**
