﻿#День4 встречаем Юлю после обеда
#
label uvao_D4_meet_Yulia_after_lunch:
#Д4 встречаем Юлю после обеда
#
# используется флаг рассказа Слави про Генду за обедом uvao_D4_lunch_sl
#
    $ persistent.sprite_time = "day"
    play sound sfx_open_door_2
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_mt_noitem_day with dissolve
#Придя, Семён приоткрывает окно, потому что домик прогрелся на солнце и читать умные книжки жарко
    "Домик успел здорово прогреться на солнце, поэтому первым делом я открыл окно нараспашку."
    if uvao_D4_concert:
# Ходили на концерт
        "В ушах до сих пор звенело от адской какофонии, которую мне приходилось терпеть последние полтора часа."
        th "И дался Славе этот концерт. Точнее я на нем."
# хорошо бы добавить описания кошмарных номеров на концерте
        th "Столько времени потрачено зря!"
        dreamgirl "Ладно, хватит ныть об упущенных возможностях!{w} Вырваться-то ты всё равно не мог. Славя сторожила как…"
        dreamgirl "Посмотри лучше, возле кровати рюкзак валяется.{w} Не про него ли Олька говорила?"
        th "А знакомый рюкзак. Точь-в-точь мой старый «Гриззли».{w} Разве что мой-то {i}дома{/i} остался…"
        th "Так и что тут нам «родители» прислали?"
        "Конфеты…"
        dreamgirl "А это точно твое? Скорее мелкой прислали. Напутали чего-то где-то."
        "Проволока… веревка… свинец… леска… ещё какая-то мелочь…"
        th "Да что за фигня? На что мне это все?"
        dreamgirl "Отлично, будем делать заграждение, отольем пуль, добудем пушку, возьмем заложника и будем требовать ответов."
        th "Да ну тебя."
        "Я задвинул рюкзак под кровать, и устало упал на неё."
        th "Что за день? Бездарно потраченное время, ненужный концерт, бесполезная посылка…{w} {i}И никаких ответов{/i}! Шикарно! Что дальше, интересно?"
        th "Ладно, посмотрю хоть учебник. Зря с риском для жизни тырил, что ли?!"
    else:
# Избежали концерта
        "Возле моей кровати обнаружился подозрительно знакомый рюкзак.{w} Можно было бы даже подумать, что это мой старый добрый «Гриззли», не будь я уверен, что прибыл сюда без рюкзака."
        th "Наверное, это про него мне Ольга утром говорила. Интересно, что там?"
        "Прямо под молнией, поверх остального содержимого, обнаружился внушительный пакет с конфетами."
        "Под пакетом - колода игральных карт, перочинный нож, моток лески, коробочка с рыболовными крючками и, почему-то, мятый кусок свинца."
        th "Странный набор. Особенно свинец этот мне прямо-таки позарез нужен… Хотя, можно из него грузил понаделать, если вдруг приспичит."
        "Отчаявшись понять причудливую логику моих «родителей», кто бы они ни были, я махнул на всё рукой и вытащил из-под подушки заветный учебник"
        th "Пора уже разобраться с этим Гендой вплотную!"
# Конец вилки с концертом
    show blinking
#    "Наверное, прошло часа два, прежде чем я отложил учебник в сторону и тупо уставился в стену."
    "Не знаю, сколько прошло времени, прежде чем я отложил учебник в сторону и тупо уставился в стену."
    "Голова была готова взорваться."
    if uvao_D4_lunch_sl:
        "По всему выходило, что Славя за обедом мне всё очень точно изложила про этого самого Генду."
        "Из книги я не узнал почти ничего принципиально нового. Так, подробности."
    else:
        th "Генда…{w} Академик из народа…{w} Верный соратник и продолжатель дела В.И.Ленина…{w} Научная работа…{w} Множество статей…{w} Важнейшая роль в становлении советской науки…{w} Беззаветная преданность идеям коммунизма…"
    play music music_list["my_daily_life"] fadein 3
    "Казалось бы, после внезапного марш-броска из промозглой зимы прямиком в середину лета я должен быть готов ко всему. {w}Оказалось, что нет, не готов."
    "Я и сам понимал, что все эти дела минувших дней меня напрямую не касаются, но ничего не мог с собой поделать. {w}Вроде бы, какое мне дело до того, кто здесь что возглавлял, но ощущение было такое, словно под ногами закачалась опора, с детства казавшаяся незыблемой."
    dreamgirl "Ой, а что тут у нас такое? Потрясение основ? Ниспровержение устоев? Чужого очкастого дядю подсовывают?"
    dreamgirl "А ну давай-ка, быстренько напомни мне основные вехи славного пути вождя мирового пролетариата {i}нашей{/i} Родины! Того самого, который Ильич!"
    th "Э-э…"
    "Память услужливо принялась подсовывать что-то про добрый прищур глаз и чернильницы из хлебного мякиша… {w}Шалаш в Разливе… {w}Или Разлив - это не местность, а что-то другое? {w}Ссылка, Надежда Константиновна и обручальные кольца, сделанные из монет…"
    "Старший брат Александр, который покушался взорвать… этого, как его… Александра III, вот!{w}\nИли нет, это-то здесь при чём. Не помню даже, кто того царя в итоге укокошил - этот самый брат, или кто-то другой?"
    "Хотя погодите, это же Александра II взорвали! И о чём это я? При чём здесь вообще все эти Александры?!"
    "Всё это на вехи пути вождя пролетариата тянуло как-то слабо."
    "Я зажмурился и попробовал ещё раз."
    "Так. Возглавлял партию большевиков, там ещё враги-меньшевики были… {w}Минуточку, так они ведь тоже были членами компартии? Вот ведь…"
    dreamgirl "Ну и какое отношение имеет та чушь, которая тебе лезет в голову, к тому, как этот самый вождь руководил страной и что он для неё сделал? Даже неважно, плохого или хорошего."
    dreamgirl "Ну ладно, последний вопрос, на двойку - назови даты рождения и смерти. {w}\nХотя нет, это слишком сложно. Хотя бы год смерти, а?"
    th "1928-й?"
    "Шиза только вздохнула. \nКажется, я сморозил очередную глупость…"
    th "Зато я Ленина в мавзолее видел! Сам, лично!"
    dreamgirl "Тогда, да! Конечно же, это полностью опровергает существование Генды, а заодно - и учебника, который валяется рядом с тобой!"
    "Шиза насмешливо фыркнула и замолчала."
    "Я задумался. {w}Получалось, что про родной мир я знал не так уж много."
    "Пожалуй, о новейшей истории здешнего мира я теперь знаю даже больше - вон, хотя бы учебник пролистал."
    "И кстати, по всему выходит, что это именно какой-то {i}другой{/i} мир. Разве что всё вокруг - очень убедительная подделка…"
    "Я снова взял в руки учебник.{w} В меру потрёпанная книга - слегка потёртая обложка, переплёт немного перекосился. Многие страницы, особенно те, что в начале, хранили следы рук предыдущих читателей.{w} Похоже, большинство из них успевало продвинуться в изучении материала не так уж далеко."
    th "Ну если уж и {i}это{/i} подделка…"
    "От размышлений о множественности миров меня отвлек негромкий шелест, донёсшийся с улицы.{w} За приоткрытым окном вздрогнула ветка сирени…"
    window hide
    $ renpy.pause(1)
    window show
    if uvao_D4_concert:
# Ходили на концерт
        dreamgirl "У нас завелись гости"
        th "Ага, и я даже догадываюсь, какие именно."
        th "Мелкие и рыжие."
        dreamgirl "Как тараканы. Непонятно, ты их гоняешь или они тебя."
        "Копошение продолжилось."
        th "Сделать, что ли, себе приятное, а ближнему гадость?{w} Тем более, Мелкая Зараза там явно не просто так засела."
        dreamgirl "Карателем подрабатываем? Одобряю! Шнель, шнель, партизанен капут!"
        th "Яволь, майн фюрер!"
        "Я встал с кровати и высунулся в окно."
    else:
# Избежали концерта
        "Похоже, кто-то там есть, причём этот «кто-то» старается не афишировать своё присутствие, раз по кустам шастает, а не ходит, как нормальные люди, по дорожке."
        "Я замер, прислушиваясь.{w} Несколько секунд всё было тихо…"
        "Потом за окном промелькнуло что-то тёмное, но так быстро, что ничего толком разглядеть не получилось."
        "Стараясь не заскрипеть пружинами, я тихонько встал с кровати и, крадучись словно ниндзя, двинулся в сторону окна{w}… Чтобы немедленно споткнуться о проклятый рюкзак, так и валявшийся на полу!"
        stop music fadeout 1
        with vpunch
        play sound2 sfx_bodyfall_1
        $ renpy.pause(1)
        dreamgirl "Не расстраивайся, у тебя есть и сильные стороны! То есть, должны быть, непременно должны…"
        "Охая, я кое-как поднялся на ноги. Хорошо хоть, головой о стол не приложился, а не то был бы у них тут детективный сюжет с моим трупом в качестве главной улики."
        "Кто бы там под окном ни прятался, после такой шумной встречи он наверняка уже смылся от греха подальше."
        "С этой мыслью я высунулся в окно."
# Конец вилки с концертом
    window hide
    scene bg int_house_of_mt_noitem_day:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.6 xalign 0.7 yalign 0.35
    $ renpy.pause(2)
    stop music fadeout 1
    scene bg ext_house_of_mt_day with dissolve:
        zoom 2.5 xalign 0.7 yalign 0.55
    $ meet('uv','Существо')
    show uv dontlike close at center
    window show
    play music music_list["mystery_girl_v2"] fadein 5
    "…Где чуть ли не нос к носу столкнулся с… э-э-э?"
    "На меня в упор смотрела пара настороженных глаз необычного золотисто-янтарного цвета."
    "Бледноватое лицо, густые, изрядо всклокоченные каштановые волосы, напряжённо расставленные уши."
    th "Что?! Уши?!"
    "Я внезапно понял, что на расстоянии вытянутой руки от меня сидит, напряжённо припав к земле, странное существо, которое я с уверенно опредилил бы как девочку-подростка, если бы не уши, больше всего похожие на кошачьи, и не боязливо поджатый кошачий же хвост."
    dreamgirl "Эй, не тупи! Неужели ничего не напоминает? Ну вспомни ты вчерашний вечер!"
    th "Да помню я всё, не мешай"
    "Пауза явно затягивалась. Не сводя с меня пристального взгляда, существо осторожно попятилось."
    show uv dontlike at center with dissolve
    "Всего-то на ширину ладони, но я почувствовал, что ещё пара секунд - и она попросту убежит."
    th "В конце концов, я всегда неплохо ладил с кошками, в отличие от собак.{w} Да и в отличие от большинства людей тоже, если уж на то пошло."
    "Опасной она мне не казалась, а если удастся наладить с ней контакт, то мало ли, что сможет рассказать такая… такое… необычное существо."
    me "Привет."
    "Негромко сказал я. Кажется, получилось не слишком уверенно, но мне было здорово не по себе."
    "Она замерла, по-прежнему глядя мне прямо в глаза."
    me "Извини, не хотел тебя напугать."
    dreamgirl "Тоже мне, мастер контакта! Тебя только с террористами договариваться посылать! Я имею в виду…"
    uv "Я думала, внутри никого нет, и вдруг ты там так загрохотал чем-то!"
    "Осуждающе сказало вдруг существо (или, всё-таки, девочка - и не поймёшь сразу, кем её считать)."
    show uv normal with dspr
    "Она наконец моргнула и, похоже, немного расслабилась."
    dreamgirl "Ты смотри, она ещё и разговаривать умеет. Надо же!"
    "Стараясь не делать резких движений, я облокотился на подоконник, попытавшись принять непринуждённую позу, насколько это было возможно с ноющими локтями и коленями."
    me "Понимаешь, я услышал, что под окном кто-то ходит, и хотел посмотреть кто, но споткнулся и упал."
    "Сказал я, решив на всякий случай строить фразы попроще."
    uv "Вы, люди, всегда такие неуклюжие."
    show uv normal with dspr
    "Сообщила она.{w} Вздохнув, уселась на траву, поджав под себя ноги и аккуратно уложив хвост вокруг. Судя по всему, убегать она раздумала."
    "Теперь, когда она перестала сжиматься в комок, я поневоле отметил, что фигурка-то у неё очень даже ничего."
    "Изрядно оборванное короткое летнее платьице не скрывало изящный изгиб бёдер.{w} Стройные точёные голени, тонкие щиколотки, маленькие ступни…"
    dreamgirl "Да что тебе ступни, ты посмотри, какие у неё…"
    th "Цыц!"
    "Призвал я к порядку одновременно и Шизу и себя."
    "Впрочем, похоже было, что хвостатую девочку нисколько не смутило столь пристальное внимание с моей стороны."
    "Наоборот, в ответ она также разглядывала меня с самой наивной непосредственностью."
    me "Э-э-э… Послушай, а как тебя зовут?"
    show uv surprise with dspr
    uv "Меня?"
    "Искренне удивилась она."
    me "Ну да. У тебя есть имя? Вот меня, например, Семён зовут."
    show uv normal with dspr
    uv "Я знаю, что Семён. Слышала, как тебя ваша старшая, которая в панамке ходит всё время, так называла. И ещё та, с длинной косой - Славя."
    uv "А меня никак не зовут. Я - это просто я, зачем мне имя? И так всё ясно."
    "Она немного подумала."
    uv "Хотя одна из ваших - мы с ней разговаривали - она меня Юлей называла. Наверное, и тебе можно, если хочешь."
    $ meet('uv','Юля')
    "Мне показалось, что беседа начала ей надоедать и я поспешил сменить тему, ляпнув первое, что пришло в голову:"
    me "А ты здесь что-нибудь искала, да?"
    uv "Я хотела посмотреть, что там у вас в домике. В других я почти во всех бывала, а тут всё время заперто, да заперто."
    show uv upset with dspr
    "Она недовольно надула губки."
    uv "Думала, может у вас там еда какая-нибудь вкусная найдётся."
    me "Так ты, наверное, есть хочешь?"
    "Догадался я."
    show uv normal with dspr
    uv "Да не то чтобы… В лесу всегда можно что-нибудь найти. Ещё я на мышей охочусь, только их поймать почему-то трудно. Странно, правда?"
    "Я-то как раз ничего удивительного в этом не находил - уши там, или не уши, а великовата она, мышей-то ловить.{w} Впрочем, ей этого говорить явно не стоило, поэтому я молча кивнул."
    uv "Ещё я в столовой еду беру иногда, только там вкусной еды обычно нет, ваши вкусную всю съедают."
    "Она сказала это так просто, что сразу стало ясно - принципы собственности, что частной, что коллективной, для неё вовсе не пустой звук.{w} Она о них попросту не знает."
    me "Слушай, так это вчера, наверное…"
    play music eat_horn fadein 5
    "Из динамиков разнёсся по лагерю призыв к пионерам восполнить иссякшие за день силы."
    play ambience ambience_int_cabin_day fadein 1
    "Я как-то сразу вспомнил, что за чтением учебника, делом пусть и полезным, пропустил полдник."
    show uv upset far with dspr
    "Юля дёрнула ушами и одним гибким движением поднялась на ноги."
    "Да-а-а, пожалуй, насчёт девочки-подростка я был неправ. Ничего детского в ней не было заметно.{w} Скорее уж, очень стройная молодая девушка, просто… компактная, что ли."
    uv "Ваши сейчас есть пойдут. Не хочу, чтобы меня кто-нибудь увидел."
    show uv upset far at fright with ease
    "Она повернулась и скользнула прочь."
    me "Подожди! Хочешь, я тебе что-нибудь вкусное с ужина принесу?"
    show uv smile far at fright with ease
    uv "Булочку! Сдобную!"
    "Живо обернулась ко мне хвостатая."
    show uv grin far
    uv "Их сегодня пекли, я знаю! Днём запах учуяла!"
    "С восторгом облизнулась она."
    me "Хорошо, будет тебе булочка. Где встретимся?"
    show uv normal far at fright
    "Юля задумалась на пару секунд."
    uv "Давай за воротами, куда автобус приезжает.{w} Там вечером обычно нет никого."
    me "Договорились…"
    hide uv with moveoutright
    "Сказал я её удаляющейся спине."
    dreamgirl "Нет, ты заметил, какие у неё…"
    th "Да заметил я, заметил! Не слепой.{w} И вообще, сделай милость - отстань. Здесь и так полно девчонок бегает, далась тебе эта ушастая!"
    dreamgirl "Вот то-то и оно, что девчонок полно, но хвост и уши - только у этой! Такая няшка!"
#    play music music_list["my_daily_life"]
    scene bg int_house_of_mt_noitem_day with dissolve
    "Со злости я хлопнул окном.{w} Хотел было пнуть валяющийся посреди комнаты рюкзак, но потом решил всё-таки поберечь ноги."
    "Кстати о рюкзаке!{w} Конфеты наверняка должны подойти для бартера с этим ушастым чудом природы!"
    dreamgirl "Позволь узнать, за какие же это услуги ты собираешься расплачиваться в таких объёмах?"
    th "За информацию! И заткнись уже наконец, или я сегодня же ночью заберусь в медпункт и буду есть там все таблетки подряд, пока не найду средство от шизофрении!"
    dreamgirl "Ладно, ладно, не горячись. Я нисколько не сомневаюсь, что способы охоты на мышей, которым она может научить, тебе очень пригодятся в жизни."
    "Недовольно буркнула Шиза, но всё-таки заткнулась."
    stop music fadeout 3
    window hide
    jump uvao_uvao_D4_supper

#    return
