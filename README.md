# [Discord-activities](https://discord.com/blog/server-activities-games-voice-watch-together)

# ENG
So, maybe I'm blind and don't know how to use the internet (or read the official wiki on this stuff), but I had trouble launching a Discord activity with custom content (the thing where you can watch YouTube, not just a status update). So, for people like me, I'm writing a very simple guide.

What we need:
- A programming language for the bot (or a service that provides one)
- A bot
- (Optional) A Discord server
- A domain/reverse proxy
- A machine to run the bot on (unless covered by the first point)

## Language

I think everyone can figure this part out on their own, but in my case, I'm using Python.
 
## Bot

A standard bot where you need to set the path.
If you already know how, [jump below](#Activity). Otherwise, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)

2. Click ```New Application``` and give your bot/app a name.

![image](https://github.com/user-attachments/assets/c1e17b49-8da6-40dd-aa48-35678843abbd)

![image](https://github.com/user-attachments/assets/fd5bb205-4c42-4d45-861b-ea5dde670e70)

3. After creating the application, go to the ```OAuth2 tab```

![image](https://github.com/user-attachments/assets/7858acb5-3ca0-4908-8edd-d8a6964ae293)

Save the ```Application ID``` you'll need it later.

<a name="Activity"></a>
4. Go to the Activities tab and enable the activity feature.

![image](https://github.com/user-attachments/assets/6a8a07f6-34fa-4815-afa9-2393bb5ea626)

You should now see its settings, which you can adjust as needed.

5. You need a domain to send interaction requests to. [Jump to this section](#Domain)

6. Once you have a domain, go back to the URL Mappings tab and insert the link in the TARGET field.

![image](https://github.com/user-attachments/assets/7f0cd3e0-39a5-4efa-ac77-9f5aef31cd8b)

7. Now, there are two options:
- If the bot already has functions, add the application (this will create a button on the bot, in the channel, or in direct messages).
- Alternatively, go to settings and enable Developer Mode under Advanced. You can also enable Application Testing, where you'll need to specify the Application ID for testing.

<a name="Domain"></a>
## Domain/Reverse Proxy

As the name suggests, this is the endpoint for our activity.
The official wiki suggests simple options like [NGROK](https://ngrok.com) and [CLOUDFLARE](https://www.cloudflare.com), but you can use any other reverse proxy or your own domain.

Both options work, but:

```NGROK```:
- +Quick and easy setup (about 1.5 minutes).
- -Can't be used in the free version (when opening the link, a warning will appear stating that you're connecting to an external server—this won't be visible in the activity, resulting in a blank window).

```Cloudflare```:
- +Works for free (if you stop before entering your card details and leave the site for a while, it won't require a card later).
- -Longer configuration (which is actually a plus, but we aim for simplicity).

## Handler

Now that we have everything—domain, bot—we just need to handle requests and set up a tunnel to the domain.
In my case, I used a VPS (but it depends on your setup; the general approach should be similar).

- Install a reverse proxy (ngrok, Cloudflare, etc.).
- Use a stub to receive data (you can use existing solutions or something more custom, but I'll leave my approach here).

## Congratulations!

By launching the tunnel (reverse proxy), handler, and bot (though the bot is only needed for setup; after that, it’s not required for basic functionality), you’ll have a working Discord activity!👍


# RUS
Итак, возможно я слепой и не умею пользоваться интернетом (а так же читать официальную вики по этой шляпе), но у меня были сложности по запуску discord активности с собственным контентом (ту штуку, в которой можно смотреть youtube, а не статус у человека), потому для людей как я пишу очень сложный гайд.

Итак, что нам потребуются:
- Язык программирования для бота (или сервис который предоставляет оного)
- Бот
- (опционально) Discord Сервер
- Домен/Обратный прокси
- И что-то на чем живет бот (если только не первый пункт)

## Язык

Ну, я думаю тут справятся все сами, но в моём случае используется Python

## Бот

Стандартный бот в котором необходимо задать путь.
Для тех кто знает спускаемся [ниже](#Активность), для остальных

1. Переходим на [Discord Developer Portal](https://discord.com/developers/applications)

2. Нажимаем ```New Application``` и даём название нашему приложению/боту

![image](https://github.com/user-attachments/assets/c1e17b49-8da6-40dd-aa48-35678843abbd)

![image](https://github.com/user-attachments/assets/fd5bb205-4c42-4d45-861b-ea5dde670e70)

3. После создания приложения перейдите на вкладку ```OAuth2```

![image](https://github.com/user-attachments/assets/7858acb5-3ca0-4908-8edd-d8a6964ae293)

Сохраняем ID приложения, понадобится далее

<a name="Активность"></a>
4. Переходим в ```Activities```, где необходимо включить саму функцию активности

![image](https://github.com/user-attachments/assets/6a8a07f6-34fa-4815-afa9-2393bb5ea626)

Далее должны появится его настройки, которые можно менять по необходимости

5. Необходим домен куда будут отправляться запросы для взаимодействий [Тык сюда](#Домен)

6. Далее, мы возвращаемся с ссылкой и переходим в вкладку ```URL Mappings``` и вставляем ссылку в ```TARGET```

![image](https://github.com/user-attachments/assets/7f0cd3e0-39a5-4efa-ac77-9f5aef31cd8b)

7. Далее несколько вариантов:
- (уже есть функции в боте)Добавить приложение (будет кнопка на боте, в канале или при личном обращении)
- Либо же, в настройках, включить режим разработчика в вкладке ```Расширенные```, (так же можно включить ```Тестирование приложения```, где уже будет необходимо указать ID приложения для тестирования)

<a name="Домен"></a>
## Домен/Обратный прокси
Из названия понятно, что нужно место обращений нашей активности.
В самой вики приводят как простые варианты [NGROK](https://ngrok.com) и [CLOUDFLARE](https://www.cloudflare.com), ну или любой другой обратный прокси, или свой домен.
Оба варианта работают, но:
- ```ngrok```:
- +Заводится и настраивается за полторы минуты
- -Не получится использовать в бесплатной версии (При переходе по ссылке будет появляться предупреждение (серверное от ngrok), что вы стучитесь туда-то туда-то ... переходите только если доверяете, но в активности его не увидеть и будет только белое окно)
- ```cloudflare```:
- +Работает бесплатно (если перейти до момента ввода карты и просто уйти с сайта на какое-то время, потом не потребуется вводит её)
- -Длительная конфигурация(вообще, это плюс, но мы в простоту)


## Обработчик

Итак, всё сделали, домен есть, бот есть, осталось обрабатывать запросы от него, да и туннель до домена было бы неплохо организовать.
В моём варианте использовался VPS (но, тут уже у кого как, но суть примерна одинакова должна быть)
- Необходимо установить приложения обратного прокси (ngrok, cloudflare, etc)
- Использовать заглушку для приема данных (можно использовать и уже имеющиеся продукты или что-то более адекватное, но свой вариант оставлю)

# Поздравляю
Запустив туннель (обратный прокси), обработчик и бота (и то не обязательно, бот нужен только для создания, потом в работе (на базовом функционале) он не требуется) мы получаем работающую активность в Discord-е 👍
