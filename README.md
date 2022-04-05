<h1>Сервис для валидации почт</h1>
Ищет домен почты в блэклисте и пабликлисте. Блэклист обновляется раз в сутки.
<br>
<br>

<h2>Проверить почту</h2>

<h3>Запрос</h3>
`GET /api/v1/check_mail/?email=example@temp-mail.com`
<h3>Ответ</h3>

    {"domain": temp-mail.com, "disposable": true, "public": false, "corporate": false}

