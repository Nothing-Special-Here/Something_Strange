# Д6-Утро
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines
#
label alt_day6_uvao_getting_up:
    $ routetag = "uv"
    $ alt_chapter(6, u"Юля. Утро")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg int_house_of_mt_sunset
    play ambience ambience_int_cabin_day fadein 4
    window show
    if alt_uvao_true:
# Будит ОД
        "Проснулся я от бесцеремонной тряски. Чья-то рука крепко ухватила меня за плечо и, похоже, просто так отпускать не собиралась."
        "С некоторым трудом глаза удалось открыть. Рука, как можно было догадаться, принадлежала вожатой."
        show mt normal pioneer close at center with dissolve2
        th "Кажется, со мной это уже было… Спасибо хоть, сегодня без перегара обошлись."
        "Действительно, в отличие от вчерашнего утра, Ольга была бодра, свежа и вполне довольна жизнью."
        "Убедившись, что я более-менее проснулся, она прекратила наконец свою импровизированную утреннюю разминку и отпустила мою многострадальную руку."
        show mt smile pioneer at center with dissolve
        mt "Семён, хватит дрыхнуть!{w} Времени восемь часов, погода отличная!"
        mt "Тем более, у меня отличные новости для тебя!"
        me "Дайте угадаю - наступил мир во всём мире?"
        "Проворчал я, отчаянно зевая.{w} Кажется, перед самым пробуждением мне что-то снилось… Что-то важное, но что именно - вспомнить никак не получалось."
#        dreamgirl ""
#        "Голос Шизы тоже показался мне каким-то заспанным."
        show mt laugh pioneer with dspr
        mt "Ну не настолько грандиозно, к моему сожалению. Но от зарядки и утренней линейки я тебя освобождаю."
        show mt normal pioneer with dspr
        mt "Кстати, снова по болезни, как и вчера, так что не забудь заглянуть в медпункт к Виолетте."
        "Она нахмурилась было, но не удержалась и прыснула, махнув рукой."
        show mt laugh pioneer with dspr
        "Вспомнив сцену за вчерашним ужином, я лишь смущённо заёрзал в кровати."
        hide mt with dissolve
        play sound sfx_close_door_1
        "Продолжая посмеиваться, Ольга проворно убежала на улицу, а я вяло принялся выпутываться из хитроумного узла, в который за ночь превратилось моё одеяло.{w} Недосмотренный сон никак не шёл из головы."
        th "И всё-таки, чте же мне снилось такое?…"
        menu:
            "Одеваться!":
                # сны - ерунда!
                "Впрочем, и в самом деле пора было уже вставать. Выспался я сегодня вволю, так что хорошенького понемножку."
                dreamgirl "Вот и молодец. Потехе время, а делу - час!{w} Ладно, за целеустремлённость тебе полагается бонус - получай свой сон!"
                # Для критиканов особо отмечу, что тру-Семён снов в Д5 не смотрел, так что пусть наверстает хоть немного
                "На меня внезапно обрушился целый ворох каких-то разрозненных обрывочных образов."
                window hide
                $ set_mode_nvl()
                window show
                # Сон Деимиург-куна
                "Насколько я смог разобрать, мне снилось, будто я проснулся посреди какого-то лагеря, причём никогда в похожем месте раньше не был."
                "Более-менее отчётливыми были образы странной девочки-брюнетки с короткой стрижкой и интересной куклой, которая выглядела как годовалый ребёнок."
                "Девочка постоянно доказывала всем, что это кукла, отрывая ей голову."
                "Ещё была злючка-вожатка, которая сразу принялась меня гнобить из-за всяких мелочей, ну и столовый бойкот запомнился - всё время, что я там провёл, я дежурил в столовой и постоянно недокладывал вожатке жратвы в знак протеста."
                "Ну и периодически подворовывал полдник…"
                "Девочку было немного жалко, она постоянно ходила одна, или сидела в сторонке и наблюдала за куклой, которая ходила сама по себе - никаких механизмов, обычная кукла…"
                "Кажется, я ее подкармливал ворованными булочками. Девочку, не куклу…"
#                nvl clear
                window hide
                $ set_mode_adv()
                window show
                "Всё остальное было совсем уж неразборчивым, так что ничего и понять было нельзя. Я ошарашенно затряс головой."
                th "Подожди, это что, и есть весь мой сон?!"
                dreamgirl "Ну так ведь никто и не обещал, что это будет «Война и мир». Хотя, как по мне, довольно креативненько получилось."
                th "Ты думаешь? Ладно, надо будет себя при случае попробовать на писательской стезе."
                "Быстро одевшись и прихватив полотенце, я отправился к умывальникам."
                jump alt_day6_true_CS_talk
            "Попытаться вспомнить сон.":
                # досыпаем…
                "Рассудив, что из-за пятиминутной задержки ничего не случится, я воспользовался проверенной методикой - закрыл глаза и постарался расслабиться, позволяя сну чуть-чуть коснуться меня."
                window hide
                show blinking
                scene black
                window show
                "Здесь главное было удерживать сознание на грани между явью и грёзой, не давая ни одной из них победить…"
                stop ambience fadeout 2
                window hide
                $ renpy.pause(5)
                scene bg int_house_of_mt_sunset
                with vpunch
                play ambience ambience_int_cabin_day fadein 2
                window show
                "…Оглушительно чихнув, я резко сел в постели, пытаясь понять, что происходит."
                dreamgirl "А вот это ты напрасно сделал."
                "Голос Шизы звучал укоризненно. Я беспомощно потряс головой, которую словно бы наполнили ватой."
                th "Что именно я сделал напрасно? Чихнул?"
                dreamgirl "Проснулся ты напрасно, бестолочь! Подождал бы ещё немного - уже пора было бы снова спать ложиться."
                "Я вглянул за часы и охнул, кубарем скатившись с кровати."
                th "Мама дорогая, вот это я вздремнул! Ещё пару часов, и если не ужинать, то уж обедать-то точно пора будет!{w} Неудивительно, что голова тяжёлая."
                "Наскоро одевшись, я решил, что немного холодной воды на мою бедовую головушку сейчас не помешает, и поскакал к умывальникам."
                jump alt_day6_true_sl_morning
    elif alt_uvao_D5_sh_mines:
        # Спалились накануне вечером ОД, знаем об аномалии немного.
        "Спал я плохо, а проснулся с жуткой головной болью. Наверное сказалась усталость вчерашнего дня – моральная и физическая. Бывает такое: вроде спал, а не отдохнул совсем. Надо будет к Виолетте Церновне зайти, взять какое-нибудь обезболивающее."
        dreamgirl "Да-да, сходи, конечно. Она тебе клизму пропишет целебную, семиведёрную. Враз вся хворь пройдёт. А уж о кошечке и думать забудешь!"
        "Шиза в своём репертуаре. Не успел я глаза открыть, а она уже комментирует. Интересно, а чем она занимается, когда я сплю? Сама с собой в шахматы играет?" # переформулировать, чтобы пол упоминался меньше
        th "А вот возьму, да и схожу"
        "Надменно ответил я своему альтер-эго."
        th "Она ведь приглашала меня к себе… {w}для беседы. Информацию какую-то обещала…"
        "Кроме того, меня беспокоила вчерашняя конфронтация с нашей любимой надзирательницей. Что-то подсказывало, что Ольга Дмитриевна этого так не оставит."
        "Я покосился на соседнюю кровать. Она ожидаемо была пуста и заправлена."
        th "Наверное вожатая на планерке у начальника лагеря. Получает заряд бодрости на весь день. За вчерашнее ЧП."
        th "А потом, надо думать, придёт давать заряд бодрости мне.{w} Нет-нет, никакой мести, мессир. Конечно же, исключительно в воспитательных целях. И исключительно методами советской педагогики."
        dreamgirl "Не забудет-не простит, можешь не сомневаться. Её здесь не для того поставили, чтобы всякие пионеры беспорядки нарушали и дисциплину хулиганили."
        th "Ладно, шутки в сторону. Пора вставать."
        "И, откинув одеяло, я начал слезать с кровати."
        play sound sfx_open_door_2
        show mt normal panama pioneer far at cright with dissolver
        "На улице послышался шум шагов и в комнату ворвалась вожатая. В который уже раз она застает меня в неглиже?{w} Я-то всего один раз её видел. Какое-то слишком неравноценное соотношение."
        "На языке крутилась фраза: \"Стучаться надо, Ольга Дмитриевна!\", но я сдержался и просто прикрылся. {w}Во первых потому, что это был прежде всего её домик, а во вторых из-за сердитого выражения лица. Видно, у начлагеря всё прошло совсем нехорошо."
        show mt angry panama pioneer with dspr
        "Вожатая остановилась посреди комнаты и вперила в меня грозный взгляд."
        me "Вы что-то хотели, Ольга Дмитриевна?"
        "Робко начал я, и тут же спохватился."
        th "Что я в самом деле рефлексую-то ? Надо избавлять от этой привычки. Тварь я дрожащая или право имею?"
        dreamgirl "Тварь-то ты конечно тварь…"
        "Ехидно прокомментировала шиза."
        dreamgirl "Шучу-шучу. Право действительно имеешь. Ты вчера такого туза из рукава достал."
        "Я прокашлялся."
        me "Что Вы хотели, Ольга Дмитриевна?"
        "Уже куда более уверенным тоном официально повторил я."
        mt "Семен, нам надо серьёзно поговорить."
        me "А можно я сначала…"
        "И показал на одеяло, обращая внимание вожатой, что я, в общем-то, ещё не одет."
        show mt laugh panama pioneer with dspr
        "Она фыркнула и пошла к выходу."
        mt "Только недолго."
        me "Само собой."
        play sound sfx_open_door_2
        hide mt with dissolve
        "Я мгновенно оделся, путаясь в шортах и рукавах рубашки. Галстук… ну его к черту!"
        mt "Ну ты всё там?"
        me "Да, можете заходить."
        "Ответствовал я, заканчивая заправлять кровать."
        play sound sfx_open_door_2
        show mt normal panama pioneer close at cright with dissolve
        mt "Так вот, Семен."
        "Начала вожатая, присаживаясь на кровать напротив меня."
        mt "Я надеюсь, что хоть какая-то часть из нашей вчерашней беседы в столовой отложилась у тебя в памяти."
        "И Ольга посмотрела на меня, видимо ожидая какой-то реакции. Но поскольку я молчал, она продолжила."
        mt "Ты вообще выводы сделал какие-нибудь?"
        "Я почесал в затылке."
        me "Да, сделал кое-какие.{w} Надо лучше прятаться в следующий раз."
        show mt angry panama pioneer close with dspr
        mt "Семен, хватит паясничать!"
        "Рассердилась Ольга Дмитриевна. Я примиряющее поднял руки."
        me "Ладно-ладно, я пошутил."
        mt "Я тебе ещё раз серьёзно повторяю – эта… это существо опасно. Очень опасно. Мы совершенно не знаем, какой может быть эффект от общения с ним. Ты ведь уже в курсе, что случилось с Александром?"
        "Я кивнул."
        mt "Скорее всего, это именно воздействие этой твоей… Юли. Мы пока не знаем, как это произошло, и обратим ли эффект.{w} А тебе, думаю, пока просто везло! И неизвестно, сколько продлится такое везение."
        "Я с недоверием смотрел на вожатую. Нет-нет, Юля это никакое не существо. Она живая и теплая. Она веселая и с ней интересно. Нет у меня никакого воздействия. А Шурик просто умственно перетрудился. С гениями такое бывает."
        "Ольга Дмитриевна с какой-то особой серьёзностью взглянула на меня и медленно проговорила."
        mt "Запомни самое главное.{w=0.8} Оно не человек.{w=0.8} Ты понял? Не человек."
        "Я обхватил голову руками. В ней роились мириады мыслей. Такое количество неприятной, непонятной информации было не так просто воспринять. Кроме того, в виски начало долбить словно молотом."
        "А вдруг вожатая права? Вдруг это началось воздействие на мой бедный, и так не очень здоровый рассудок? Закончить свои дни в комнате, обитой матрасами?{w} Нет, нет… Я отказываюсь принимать такое…"
        show mt normal panama pioneer close with dspr
        "Ольга терпеливо ждала моей реакции."
        mt "Вижу, что ты до сих пор до конца мне не веришь. Что ж, не в моих силах заставить тебя. В таком случае - {w}Будь.{w} Очень.{w} Осторожен."
        mt "Я не знаю всех подробностей, но Виолетта Церновна должна знать больше. Думаю, тебе стоит навестить её."
        show mt smile panama pioneer close with dspr
        mt "Но только после завтрака. Ты ведь помнишь : здоровое питание прежде всего."
        "Она легонько улыбнулась и ушла."
        hide mt with dissolve
        "Линейку, с этой лекцией о паранормальных явлениях, я пропустил. И слава рандому. Интересно, кто её проводил, если вожатка здесь была?{w} Славя наверное, как обычно. Ей не впервой."
        "Остается нерешенным лишь один вопрос. Верить или не верить словам вожатой?"
        "С одной стороны, ведь не одна Ольга меня пугает. Виола тоже не остается в стороне."
        "С другой стороны, это может быть просто коллективная работа по воспитанию подрастающего поколения. Осталось только Саныча на меня натравить. С каким-нибудь страшным рассказом."
        menu:
            "Завтрак прежде всего!":
                pass
                # Умываемся ("Неосознанно приобретаю полезные привычки, хех..."), идем в столовую
                # пока стоим в очереди на раздаче, приходит Виола, получает паек без очереди и приглашает на беседу за начальственный стол.
            "Поговорить с Виолой":
                pass
                # Бежим в медпункт, застаем Виолу в дверях - собиралась на завтрак.
                # Беседа.
    else:
        "Спал я как убитый. А проснулся с ощущением, что мои руки отделили от тела и оставили где-то в другом месте. Наверное вчерашняя переноска Шурика (будь он неладен) виновата. Вставать не хотелось. Я с наслаждением потянулся."
        "Наши рученьки устали, мы таскали, мы таскали…"
        th "Интересно, как он будет отмазываться сегодня?"
        dreamgirl "Интересно, как сегодня будешь отмазываться ТЫ?"
        "Хихикнула Шиза."
        me "А я-то за что ?"
        dreamgirl "Да ведь тебя вчера с утра никто не видел. И на завтраке ты не был. И на зарядке тоже. И линейку пропустил. И не поучаствовал ни в одном лагерном мероприятии. В общем ты ужасный пионер, Семён"
        "И Шиза снова залилась ехидным смехом."
        "Быстро одевшись я пошёл в сторону умывальников."
        window hide
        scene bg ext_house_of_mt_day with dissolve
        play sound sfx_close_door_1
        $ renpy.pause(1)
        scene bg ext_washstand_day with dissolve
        $ renpy.pause(1)
        scene bg ext_washstand2_day with dissolve
        play sound sfx_open_water_sink
        $ renpy.pause(1)
        play sound_loop sfx_water_sink_stream
        window show
        "Умывание-умывание… Брр… Эту пытку ледяной водой наверное Генда придумал, не иначе."
        "И такая экзекуция каждый день. Но результат всё же каждый раз радует - бодрость духа и тела в наличии. И сон прогоняет на раз-два. Закаляйся, если хочешь быть здоров…"
        "А теперь \"продолжим наши игры, как говорил редактор юмористического журнала, открывая очередное заседание и строго глядя на своих сотрудников\" - то есть пора идти на зарядку."
        window hide
        play sound sfx_close_water_sink
        stop sound_loop
        play ambience ambience_camp_center_day
        scene bg ext_square_day with dissolve
        $ persistent.sprite_time = "day"
        $ day_time()
        window show
        "На площади как всегда многолюдно. Традиционные махи и наклоны под предводительством жизнерадостной Слави, невыспавшиеся лица пионеров – всё как обычно. Всё-таки и от ежедневной лагерной рутины есть какая-то польза."
        "А теперь линейка. Я наперёд знал последовательность событий. Вот из толпы выходит Славя, чеканя шаг. Подходит к вожатой, делает салют. Идёт к флагшотку. Кажется сегодня меня не позовут поднимать флаг."
        dreamgirl "Ты расстроен? Я лично очень."
        "И Шиза притворно шмыгнула носом."
        "Алое полотнище взмывает к небу. Всё-таки есть что-то магическое в поднятии флага, есть."
        "А теперь должен быть сигнал на завтрак. Но… похоже сегодня возникли какие-то изменения в привычном лагерном графике."
        show mt normal pioneer far with dissolve
        "На середину площади вышла Ольга Дмитриевна. Я вдруг почувствовал неладное."
        dreamgirl "Готовься, чувак" 
        "Прошептала мне Шиза, подтверждая мои подозрения."
        mt "Пионеры, внимание."
        "Сказала вожатая, обращаясь сразу ко всем."
        "Ребята загалдели, лица их выражали разочарование и недовольство. Похоже они, как и я, не понимали, почему вместо завтрака должны выслушивать какие-то незапланированные речи вожатой."
        "Но у Ольги Дмитриевны очевидно был большой опыт в подавлении мятежей на кораблях."
        show mt angry pioneer with dspr
        mt "А ну-ка тихо!"
        "Она повысила голос всего лишь слегка, но и этого – удивительное дело - оказалось достаточно: все сразу же замолчали. Всё-таки авторитет это большая сила."
        show mt normal pioneer with dspr
        mt "Семён." 
        "Теперь она обращалась ко мне."
        #TODO: Музычка неприятностей, алисочкина тема вроде.
        mt "Выйди-ка сюда."
        "Мне ничего не оставалось, как выйти в центр площади на подгибающихся ногах. Ненавижу толпу. А если ещё ты знаешь, что тебя сейчас ожидает публичная порка перед этой самой толпой, то дело вообще труба."
        mt "Не потрудишься-ли объяснить своё вчерашнее отсутствие на зарядке, линейке и завтраке?"
        "Строго спросила у меня вожатая."
        me "Я это… гулял…"
        "Пролепетал я."
        th "Блин! И почему я её боюсь-то? Мужик я или не мужик, в конце-концов? Надо расправить плечи и ответить ей что-нибудь этакое."
        dreamgirl "Чувак! Это называется субординация. Не ты это придумал и не тебе это менять."
        me "Я гулял, гулял… и заблудился. Вот!"
        mt "Интересно, где же ты это гулял, что заблудился?"
        "Похоже вожатой моя версия вчерашнего отсутствия ни на минуту не показалась правдоподобной."
        me "А я в лес гулять ходил. Грибы там знаете, ягоды…"
        "Мой голос звучал всё менее уверенно. А Ольга Дмитриевна мрачнела всё больше."
        show mt angry pioneer with dspr
        mt "Так. Значит ты ещё и покидал территорию лагеря."
        "Зловещим тоном начала она."
        mt "Ты ведь знаешь, что пионерам запрещено покидать территорию оздоровительного учреждения. Без сопровождения взрослых"
        "Пионеры молча внимали речам вожатой. Похоже каждый из них был рад, что не он оказался на моём месте. А я был бы рад отказаться от этой роли и поменяться с кем-нибудь, но никто не вызвался. Поэтому пришлось стоять и выслушивать нравоучения."
        show un shy pioneer far at fright with dissolve
        "Краем глаза я заметил сочувственный взгляд Лены. Она, в свою очередь, заметила, что я смотрю на неё и покраснела, но глаза не отвела."
        hide un with dissolve
        "Некоторые пионеры уже начали высказывать недовольство задержкой традиционного кормления, которому я послужил невольной причиной."
        show mt normal pioneer with dspr
        mt "Так. Спокойно, пионеры. Я уже заканчиваю."
        mt "Ты всё понял?"
        "Обратилась ко мне вожатая."
        "Оказалось, что последние пару минут болтовни вожатки я пропустил мимо ушей. Но не признаваться же в этом?"
        me "Да, да, конечно, Ольга Дмитриевна."
        "Соврал я."
        me "Оправдаю и исправлюсь, больше не повторится."
        play sound eat_horn fadein 2
        mt "Прекрасно. А теперь все могут идти завтракать."
        hide mt with dissolve
        "И как по заказу раздался сигнал горна. Она что, всё предусмотрела?"
        stop sound fadeout 2
        dreamgirl "Так, а здесь у нас непоняточки."
        "Возмущённо фыркнул мой внутренний собеседник."
        dreamgirl "Почему это тебя допросили с пристрастием, а вчерашнего героя дня Шурика свет Арматуровича - нет ? Он-то кажется провинился не меньше, а то и побольше нашего."
        "В кои-то веки я был согласен с Шизой. Но логику вожатой мне, похоже до конца не понять…"
        jump alt_day6_uvao_breakfast
        window hide
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full
        window show
        "Столовая была уже битком. Неудивительно. Свободными оставались всего пара столов. Один возле окна, где всегда в одиночестве принимал пищу какой-то пожилой пионер (а может и не пионер) с незапоминающимся лицом. А другой возле Электроника и Шурика." #Толик? Пожилой? Серьёзно?
        "Удача! Они-то мне и нужны. Может быть удастся что-нибудь узнать про вчерашние фортели этого гладиатора. Возможно Шурик доверяет Элу и будет с ним откровенен."
        "Взяв на раздаче традиционные утренние бутерброды и кофе, я отнёс поднос за выбранный стол и сел так, чтобы держать в поле зрения обоих кибернетиков."
        #TODO: Эмоции хакиров
        show sh normal pioneer far at right
        show el normal pioneer far cright
        with dissolve
        sh "…ты же знаешь, что у нас деталей для робота не хватает катастрофически. А я тут недавно разбирался на чердаке клубов и нашёл план-схему старого корпуса, который здесь недалеко."
        el "Да знаю я, что здесь недалеко находится старый заброшенный корпус. И что в нём может быть интересного?"
        sh "Да ты дальше слушай!"
        show sh serious pioneer far at right with dspr
        "Было заметно, что Шурик сильно возбуждён. Главное, чтобы он опять с катушек не съехал."
        "Похоже, что Электроник подумал о том же самом, потому что с тревогой сказал:"
        el "Шурик, ты главное спокойнее."
        "Шурик глубоко вздохнул несколько раз и кажется взял себя в руки."
        sh "Так вот. Оказывается этот корпус совсем не то, чем кажется. Под его территорией располагается сложная система тоннелей и бункеров. Вероятно на случай какой-то техногенной катастрофы. Или, что более вероятно, для каких-то исследований."
        "По лицу Электроника было видно, что он считает рассказ своего друга не более, чем горячечным бредом, вызванным переутомлением, но вслух он ничего не сказал. Вот, что значит воспитание."
        "Видимо, решив пока принять на веру рассказ о тоннелях, бункерах и техногенных катастрофах, он мягким тоном обратился к Шурику."
        dreamgirl "Правильно. С сумасшедшими спорить низзя"
        el "Так, допустим. А зачем ты туда пошёл?"
        sh " Ну я же говорю – найти каких-нибудь радиодеталей. Для робота. Там ведь наверняка есть много всякой аппаратуры."
        "Логика в его словах несомненно была. Видимо поэтому Электроник проглотил и это."
        "Но всё же спросил. И как мне показалось, даже немного обиженно. Как же - вместе делают общее дело, а тут на тебе."
        el "А почему ты меня не позвал с собой?"
        sh "Хотел тебе сюрприз сделать."
        "Мгновенно отреагировал Шурик."
        sh "Ты придёшь в клуб, скажешь: \"Затянулся наш проект. Месяц уже стоит. Жаль, что у нас нет резисторов серии Е24\". А я тебе: \"Да вот же они\". И мы сможем наконец закончить нашего робота и заняться другим проектом." #…родим двоих деток, получим мильйон и будем жить долго и счастливо, ага.
        "Видно было, что к разговору он подготовился основательно. Но сможет ли он убедить вожатую в своей правоте и невиновности также легко, как Электроника ? Кроме того, оставался невыясненным и ещё один момент."
        "Кажется Электроник тоже вспомнил про этот самый момент, потому что понизив голос спросил:"
        el "Шурик. А чем было вызвано твоё внезапное нападение и неадекватное поведение?"
        "Шурик помрачнел."
        sh "А вот это самое интересное. Дело в том, что я ничего не помню. Я помню как спускался в тоннель. И всё, потом провал. А в следующий момент меня уже бьёт по лицу Ольга Дмитриевна."
        sh "Больно, кстати."
        "Он потер щёку."
        "Электроник сидел какой-то притихший, переваривая полученную информацию. Но длилось это недолго - видимо инстинкт учёного преобладал."
        dreamgirl "Дух преобладал над плотью, ага"
        el "Возможно подобное неадекватное состояние и провалы в памяти - так называемая антероградная амнезия - вызваны травмой головы. Ты нигде не падал?"
        sh "Вроде нет."
        el "Какова же может быть причина в таком случае? Переутомление, возможно? Или что-то другое?"
        "Электроник задумался, перебирая варианты и что-то шепча про себя."
        sh "У меня есть теория. Даже две. И они даже могут быть связаны."
        sh "Первая. Непроветриваемые десятилетиями тоннели, соответственно недостаточный приток свежего воздуха что приводит к кислородному голоданию."
        sh "Вторая. Возможно в тоннелях произошла утечка какого-то газа, вызывающего временное изменение сознания."
        sh "К такому выводу меня привёл странный запах в катакомбах."
        el "Но это звучит как-то уж совсем фантастически."
        sh "И тем не менее, это может быть правдой."
        "В самом деле, вся эта история выглядела фантасмагорией, особенно последняя её часть. Было заметно, что Шурик всё это придумал от начала до конца. Но только не Электронику. Видимо он полностью доверял своему другу. Но вот оправдает ли этот друг такое доверие…?"
        "Курносый нос Электроника задрался, глаза горели. Видно было, что он уже мысленно строил теории относительно поведения Шурика в катакомбах и ему уже не терпелось вернуться в клуб и произвести какие-нибудь расчёты."
        "Поняв, что здесь я больше ничего не узнаю, я поднялся с места, отнес поднос с посудой в мойку и пошёл к выходу из столовой."
        jump alt_day6_uvao_duty
#Хозработы
label alt_day6_uvao_duty:
    $ alt_chapter(6, u"Юля. Хозработы")
    # Надо наверное Юлю навестить. Или лучше всё-таки сходить после обеда ? И сделать это надо как можно незаметнее. А то мне как будто сегодняшней взбучки мало. Кроме того, в обед булочки будут. А я как раз Юле обещал. Не идти же с пустыми руками.
    # Решено: возьму какое-нибудь поручение от вожатой и свалю по тихому. Осталось придумать это самое поручение. И желательно подальше от центра лагеря. Что бы такое придумать ?
    # Но придумывать мне ничего не пришлось. У выхода из столовая меня уже ждала Ольга Дмитриевна собственной персоной.
    # ОД: -Вот и ты, Семен. Прекрасно. Пойдём, прогуляемся.
    # Я мысленно застонал. Ну что же это такое.. ? 
    # Ш: "Это карма, чувак. Смирись. А ещё лучше посмотри на это с другой стороны. Ведь ты искал повод уйти из лагеря. А теперь у тебя есть официальная причина – ты выполняешь поручение вожатой."
    # Чего-чего, а логического мышления у Шизы не отнять.
    # Ш: "А то !"
    # Ш: "Учись пока я здесь"
    # С: "И самодовольства тоже."
    # Ш: "Эй. А вот это уже было обидно!"
    # Надеюсь я не кажусь со стороны полным тормозом, когда проходят вот такие внутренние беседы..
    # А мы между тем прогулочным шагом шли по дорожке. Нас обогнали кибернетики, спеша по каким-то своим кибернетическим делам.
    # ОД :-Семен, я не стала говорить этого при всех. Ты вчера хоть и провинился отчасти, но есть некто, кто провинился ещё больше. Пусть и неумышленно, возможно.
    # Ш: "Ну наконец-то. Справедливость восторжествовала ! Аве, Ольга Дмитриевна !"
    # Я не обратил внимания на кривлянье Шизы. Не до того сейчас.
    # С:- И этот некто – Шурик, если я верно понимаю ситуацию. 
    # ОД: - Совершенно верно.
    # Кивнула она головой.
    # ОД: -Если честно, он меня вчера напугал довольно сильно. Такая неожиданная вспышка агрессии со стороны всегда спокойного человека. 
    # ОД: -Он ведь мог кого-нибудь серьёзно покалечить.
    # С: -Запросто. Он вообще страшный человек.
    # Вожатая нахмурилась.
    # ОД: -Семен, прекрати паясничать пожалуйста. В этом лагере хоть у кого-нибудь есть капля рассудительности ?
    # ОД: -Так вот, друг ты мой ситный. Я ведь не сказала, что проступок Шурика аннулирует твой.
    # ОД: -Расскажи-ка мне, где ты всё-таки вчера был первую половину дня? Почему ты вернулся такой грязный ?
    # С: -Я же говорю: ходил по грибы, по ягоды. Поскользнулся, упал..
    # Ш: "Очнулся – гипс"
    # Ожидаемо хохотнула Шиза.
    # ОД: -Не думай, что я поверила в твои сказки на линейке.
    # Спокойно сказала вожатая.
    # С: -Мне больше нечего вам сказать.
    # Я пожал плечами. 
    # Тогда Ольга Дмитриевна, видимо решив зайти с другого конца, спросила:
    # ОД:- Семен, а ты вчера не видел ничего необычного, подозрительного ?
    # ОД: -Сам понимаешь, у нас тут всё-таки внештатная ситуация. Шурик пострадал, мы сами чуть не пострадали.. 
    # ОД: - Как вожатая, я обязана провести расследование.
    # ОД: -А там, где ты вчера собирал грибы, ягоды.. Кстати, напомни, где это было ?
    # И она выжидающе посмотрела на меня. 
    # Ну Ольга Дмитриевна, ну тонкий психолог ! Ага, щас. Так я всё и рассказал.
    # С: -Нет, ничего необычного не было.
    # Я снова пожал плечами. 
    # Видимо вожатая поняла, что больше от меня ничего не добьётся.
    # ОД: -Значит говорить ты не хочешь. Прекрасно.
    # ОД: - Покидание пределов оздоровительного учреждения пионерами без сопровождения взрослых категорически запрещено. 
    # ОД:- Поэтому ты должен понести заслуженное наказание..
    # С:-А как же..
    # Начал я, вспомнив вчерашние мытарства с Шуриком.
    # Но Ольга Дмитриевна жестом остановила меня.
    # ОД: -Но поскольку ты вчера принял активное участие в поисково-спасательных работах и показал себя надежным товарищем, на которого можно положиться, то наказание частично аннулируется.
    # С: - Спасибо Ольга Дмитриевна ! Я..
    # Она снова остановил меня.
    # ОД: -Я сказала – частично.
    # Поэтому, чтобы загладить свою вину полностью, ты сегодня ты весь день будешь работать на благо общества. И если будешь продолжать в том же духе, тогда, возможно, когда-нибудь ты станешь образцовым пионером. 
    # И она замолчала, наконец оставив меня в покое. Надолго ли ?
    # Тем временем мы подошли к сцене, где суетился Электроник. Он что-то подкручивал отверткой в неудобной позе и пыхтел от натуги. На лавках сидели ребята разных возрастов. Они весело болтали и смеялись.
    # Мимо прошла жизнерадостная и активная, как всегда, Славя. Эх, мне бы хоть капельку её энергии и оптимизма !
    # ОД: - Сергей, принимай помощника !
    # Крикнула вожатая.
    # Тот распрямился и явно обрадовался.
    # ОД: -Семен тебе поможет принести и расставить аппаратуру.
    # ОД: - И чтобы сегодня к вечеру всё было готово !
    # Э: - Конечно, конечно, Ольга Дмитриевна. 
    # Затараторил кибернетик.
    # Э: - К вечеру всё будет готово, не беспокойтесь.
    # Э: -Мы с Семеном всё сделаем.
    # Я с тоской посмотрел в сторону сцены. Да, многолюдно здесь. Сбежать явно не получится.
    # Но ничего, ещё не вечер..
    # С: -Кажется меня об этом как-то забыли спросить..
    # Пробурчал я про себя.
    # ОД: - Что ты говоришь, Семен ?
    # Притворилась, что не расслышала вожатая.
    # С: - Я говорю, что здесь же других ребят полно. И Славя вот например. Кроме того, у Электроника Шурик есть. Они в паре лучше работают.
    # ОД: -Семен.
    # Строго сказал вожатая. 
    # Как же она обожает эти нравоучения.
    # ОД: - Во первых, ты наказан, не забывай об этом. Во вторых, Шурик плохо себя чувствует, ты прекрасно знаешь об этом. В третьих, Славяна девочка. Неужели ты позволишь девочке выполнять мужскую работу, где требуется физическая сила ?
    # ОД: - Так что за работу. А я потом приду и проверю.
    # И выполнив свою назидательную миссию, она удалилась.
    # Я бы лично позволил. Мне совсем не улыбалось таскать здоровенные колонки и усилители по всему лагерю.
    # Ш: "Эх ты, джентльмен.."
    # А ещё лучше я бы нагрузил все эти тяжести на Шурика.
    # Ш: "А вот это уже хорошая идея"
    # Хихикнула Шиза.
    # С: "Но не осуществимая"
    # Тем временем ко мне подошел отвратительно жизнерадостный Электроник.
    # Э: -Ну что, Семён, поработаем ?
    # Весело спросил он.
    # С: - Сработаемся.
    # Мрачно ответил я. 
    # Этот разговор вдруг почему-то напомнил мне сцену из какого-то фильма.
    # С: -Эл, скажи, а у вас в лагере несчастные случаи были ?
    # Э: - Нет, никогда. А почему ты спрашиваешь ?
    # Удивился кибернетик.
    # Сл (Славя): -Семен, что ты такое говоришь ?
    # Строго спросила подошедшая Славя.
    # Сл: -Какие ещё несчастные случаи ? 
    # Сл: -Пойдемте мальчики, у нас работы полно. Из клуба много чего перенести надо.
    # И мы втроем отправились в музыкальный клуб. В этот раз Мику не сидела под роялем, а вполне себе репетировала какую-то песню. Наверное репертуар на вечер подбирает.
    # М: -Привет, ребята ! Как хорошо, что вы зашли.
    # Защебетала болтушка и махнула головой, отчего длиннющие ультрамариновые хвосты её волос прыгнули вверх-вниз. Я невольно залюбовался.
    # М: -А мне Ольга Дмитриевна уже всё рассказала. Вечером будет концерт. Художественная самодеятельность. 
    # И Мику от удовольствия зажмурилась.
    # М: - Я буду играть и петь. Я много на чем умею играть, честно-честно. На гитаре, на барабанах и на флейте ещё. 
    # М: -И другие ребята будут играть. А ты, Семочка, играешь на чём-нибудь ? А ты, Сережа ?
    # Сл :- Подожди, Мику.
    # Остановила девочку-оркестр Славя. 
    # Сл: - Нам нужны инструменты и аппаратура.
    # М: -Конечно-конечно, берите. Вот гитары, вот барабанная установка, вот усилитель, а вот здесь колонки. 
    # Говорила она, показывая на озвученные предметы.
    # М: - А вот шнуры ещё. И стойки для микрофонов.
    # Я почесал затылок, оглядывая всё это музыкальное добро. Много. За один раз-то и не унести. Но уж взялся за гуж..
    # И вот уже второй раз мы с Электроником стали товарищами по несчастью в переноске всяких тяжелых и бесполезных грузов. 
    # Проклятый усилитель оттянул мне все руки, а несчастные две сотни метров от клуба до сцены показались марафонской дистанцией. Почему здесь так распространен ручной труд ? Мы занесли деревянного монстра по ступенькам и с усилием поставили на дощатый пол сцены. 
    # Я присел на край сцены, тяжело дыша. Болели руки. Электроник пристроился рядом. С меня градом лил пот. По лицу кибернетика было видно, что он чувствует себя не лучше. А ведь ещё четыре колонки, каждая из которых весит как половина усилителя..
    # С: -Передохнём пару минут.
    # Предложил я.
    # Эл: -Ага.
    # Сл: -Семен, помоги пожалуйста.
    # Позвала Славя. Она расставляла по сцене микрофонные стойки. 
    # Блин ! Ну почему я-то сразу ?
    # Пришлось встать и подойти.
    # С: -Что такое, Славя ?
    # Спросил я, по возможности изображая дружелюбие.
    # Сл: -Семён, ты устал ?
    # Заботливо спросила активистка.
    # С: -Есть немного.
    # Небрежно кивнул головой я.
    # С: -Ничего страшного.
    # С:- Не надо обо мне беспокоиться. Беспокойся вон, о нём.
    # И показал на Электроника. 
    # Сл: -Да с ним всё будет в порядке.
    # Отмахнулась Славя.
    # Сл: -Другое дело ты..
    # Как-то она это по особому сказала. Я внимательно посмотрел на девочку.
    # И выглядит она сейчас как-то иначе. 
    # С: -А что я?
    # Сл: -Ну ты же вчера ещё днем где-то упал. Грязный ведь пришёл какой.
    # Сл: -А потом ещё Шурик тебя стукнул. Тебе больно наверное было ? Бедный..
    # Почти промурлыкала Славя. Да она, что, флиртует со мной? 
    # Ш: "Вот оно ! Не упускай своего шанса. Девки на тебя штабелями вешаются, гусар"
    # Ш: "Как говорится – дамы легли и просят"
    # С: "Нет, так нельзя. Что же, меня пальчиком помани и я пойду ? Пусть знает, что меня голыми руками не возьмёшь. Голыми ногами, разве что. А ножки у Слави ничего, кстати".
    # Ш: "Ах да, у тебя же вариантов дохрена. Понравился ты девочке, не видишь что-ли ?"
    # Я внимательно посмотрел на Славю. Она также внимательно смотрела мне прямо в глаза.
    # С: -Ну допустим не стукнул.
    # Спокойно отпарировал я.
    # С: -Я просто поскользнулся. Вот и всё.
    # С: - Что делать-то надо ?
    # Сл:- Да нет, нет, ничего..
    # Как-то рассеяно ответила она и отошла.
    # Я пожал плечами. Не хотите – как хотите. Эх, сбежать бы к Юле сейчас !
    # Но боюсь не получится, пока всю аппаратуру не перетаскаем. Но вот потом, когда концерт начнётся, за мной уже не будут так пристально следить..
    # Но как всегда планы мои были нарушены. В этот раз подбежавшей Ульянкой.
    # У:- Семён, там тебя ОльДмитревна искала. Сказала, чтобы ты домой шёл немедленно.
    # И она также быстро растворилась в кустах. Какой-то ниндзя просто.
    # Так, а если я уйду, кто же у нас будет выступать в роли вьючной лошадки ? Впрочем это уже не моя забота. У меня официальный повод – вызов к вожатой. Интересно, что ей от меня понадобилось ?
    # С такими мыслями я удалился. Славя проводила меня задумчивым взглядом. Да, с ней явно что-то не то.
    # Я зашёл в наш с вожатой домик.
    # С: -Вы меня искали, Ольга Дмитриевна?
    # Вожатая лежала на кровати с книгой в руках. Интересно, что читают вожатые? Не любовные же романы ? Хотя с нашей станется.
    # ОД: - Да, Семён. У меня к тебе серьёзный разговор.
    # Сказала Ольга Дмитриевна, откладывая книгу в сторону. Я присмотрелся к обложке. Так я и думал. "Унесенные ветром", Маргарет Митчелл. После дамского чтива серьёзные разговоры самое то.
    # ОД: -Семен.
    # Мягко начала вожатая, принимая сидячее положение.
    # ОД: - Я ведь всё равно узнаю, где ты был вчера. Лучше расскажи всё сам. Как говорится, признание своей вины смягчает наказание.
    # С: -Опять начинается ?
    # Возмутился я. Впрочем не очень сильно.
    # ОД: -Да, Семен, да. Начинается. Это моя обязанность - знать всё обо всех.
    # ОД: -А также моя обязанность заботиться обо всех. Вот ты отсутствовал половину дня.
    # ОД: -Усталый, голодный. А потом твои родители с меня спрашивать будут ведь, почему их мальчик так исхудал.
    # С: -Да не был я голодный. 
    # Возмутился я.
    # С: -Меня Юля покормила орехами.. 
    # И тут же зажал себе рот рукой. Блин ! Что же я наделал ?!
    # ОД: -Это кто такая ?
    # Нахмурилась вожатая.
    # С: -Девочка одна знакомая.
    # Вяло попытался отбрыкаться я. Но вожатую было уже не остановить.
    # ОД: - Семен, не ври мне хоть в этот раз. Я знаю всех детей в этом лагере. Никакой "Юли" среди них нет.
    # Что же делать ? Эх, была –не была. Да и что мне теперь уже остается, загнанному в угол ?
    # С: - Помните, я вам рассказывал про своё видение девочки с кошачьими ушами и хвостом ? Так вот она на самом деле существует. Да-да ! Её зовут Юля. Она живёт в катакомбах под старым корпусом, ловит мышей и делает запасы грибов на зиму. Вчера я ходил к ней в гости провёл там всю первую половину дня. 
    # Видимо это невероятное объяснение произвело впечатление на вожатую, потому что глаза её округлялись всё больше и больше с каждой моей фразой. А в конце этой пространной речи она смотрела на меня уже с неподдельным испугом. Более того – я мог бы поклясться, что вожатая была в ужасе !
    # ОД: -Семён ! Ты, с этой кошкой ! Никогда не смей больше подходить к ней ! Она опасна !
    # ОД : -Ты с ней контактировал ! Ты мог пострадать ! 
    # Кажется она немного успокоилась.
    # ОД : -Сейчас мы немедленно пойдём к доктору Виоле. Тебя надо обследовать. 
    # И она вскочила с кровати, направившись в сторону двери.
    # С: -Да со мной всё нормально ! 
    # Но к сожалению, слова мои не возымели никакого эффекта. Пришлось встать и пойти вслед за вожатой.
    # pass
#