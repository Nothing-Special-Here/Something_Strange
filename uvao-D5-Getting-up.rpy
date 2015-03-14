# Д5-подъём
#
# используется флаг выхода на тру-энд alt_uvao_true
#
label alt_day5_uvao_getting_up:
    $ routetag = "uv"
    $ alt_chapter(5, u"Юля. Утро")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg int_house_of_mt_sunset
    play ambience ambience_int_cabin_day fadein 4
    window show
    if alt_uvao_true:
        #Будит ОД
        mt "Семён! Семён!" with hpunch
        th "М-м-м…"
        mt "Семён!" with hpunch
        "Голос продолжал неумолимо ввинчиваться в голову, а плечо неумолимо продолжали трясти, и мне пришлось-таки открыть глаза."
        show mt angry pioneer close at center with dissolve
        "Надо мной нависало недовольное лицо Ольги."
        me "Ох… Ольга Дмитриевна… Что случилось?"
        mt "Семён, вставай давай!"
        "Я обречённо вздохнул… И удивлённо раскрыл глаза!"
        "Исходящий от вожатой сложный букет запахов наводил на совершенно определённые мысли:"
        show mt sad pioneer at center with dissolve
        dreamgirl "Коньяк. Вчера. Много."
        "Я сел в постели.{w} Внешность вожатой при ближайшем рассмотрении подтвердила догадку Шизы - лицо имеет откровенно зеленоватый оттенок, одежда мятая…"
        mt "Семён, вставай!"
        "Ольга слегка покачнулась и, поморщившись, поспешно присела на свою незаправленную кровать."
        "Судя по тому, как мне хотелось спать, до подъёма было ещё далеко и я решил снова уточнить:"
        me "Ольга Дмитриевна, так что случилось-то?"
        mt "Да ничего не случилось, нам идти пора. Мне на летучку…"
        "Тут она снова поморщилась."
        mt "…И тебе тоже есть куда!"
        "Не удержавшись, я протяжно зевнул."
        me "Так а мне-то зачем в такую рань идти?"
        mt "Сам знаешь, пока поздняя пташка…"
        "Тут она попыталась улыбнуться, но немедленно осознала всю опрометчивость своего поступка и схватилась за голову."
        show mt angry pioneer at center with dspr
        mt "Короче говоря, марш по делам, пока ещё всё тихо! Мне совсем не надо, чтобы весь лагерь знал о том, что один из моих пионеров оставил территорию и шляется неизвестно где."
        show mt normal pioneer at center with dspr
        mt "Если что - на мероприятиях ты с утра отсутствовал, потому что приболел, Виолетта подтвердит."
        "Кажется, столь длинный монолог её окончательно утомил, потому что она замолчала, махнув рукой."
        "Потом с некоторым трудом поднялась, взяла со стола какой-то пакет и сунула его мне."
        play sound sfx_paper_bag
        mt "Это тебе вместо завтрака, перекусишь по дороге."
        dreamgirl "Монстр перегарный! Как будто после завтрака нельзя было пойти!"
        "Подойдя к двери, Ольга сердито обернулась."
        show mt angry pioneer at center with dspr
        mt "Семён, да вставай ты уже! И только попробуй мне снова заснуть!"
        hide mt with dissolve
        play sound sfx_close_door_1
        "После этого она освободила наконец помещение. Вздохнув, я встал и принялся одеваться."
        "В пакете оказались несколько сдобных булок со вчерашнего ужина. Недолго думая, я сунул пакет в рюкзак."
    else:
        #Встаём сами
        play sound_loop phone_vibro fadein 2
        "Проснулся я от какого-то неприятного жужжания."
        th "Вибровызов…"
        "Не открывая глаз, привычно потянулся было вправо, чтобы добраться до стола и заткнуть этот чёртов телефон{w}… И уткнулся носом в стену!"
        th "Что?…"
        "Через пару секунд до меня дошло, что я же не дома!"
        stop sound_loop fadeout 1
        "Я спустил ноги с кровати, достал из-под подушки телефон и выключил наконец будильник."
        "Потряс головой, прогоняя остатки сна и попытался сфокусировать взгляд на экране. «6:47»"
        "Вожатой, как я и рассчитывал, не было."
        th "У неё сейчас летучка, наверное…{w} Как раз успею собраться и свалить по-тихому…{w} Пока ещё меня хватятся…"
        th "…"
        "Тут я обнаружил, что ноги мои по-прежнему касаются прохладного деревянного пола, а вот туловище уже безвольно завалилось набок…{w} Голова коснулась вожделенной подушки…"
        dreamgirl "Пра-а-авильно, плюнь ты на эту возню. Завтра сходишь. Или послезавтра."
        "Насмешливо шепнула мне Шиза."
        "Со стоном я выволок себя из постели и встал, покачиваясь, посреди комнаты."
        th "Господи, как спать-то хочется…"
        "Всё-таки через пару минут я наконец-то проснулся достаточно, чтобы заняться хоть какой-то осмысленной деятельностью{w} - для начала, одеться."
    play music music_list["everyday_theme"] fadein 5
    th "Так… Смартфон в карман…{w} Конфеты с булками в рюкзаке…{w} Штаны на мне. Ничего больше не забыл?"
    "Подумав, на всякий случай переложил перочинный ножик из рюкзака в карман."
    "Я широко зевнул напоследок, чуть не вывихнув челюсть, закинул рюкзак на плечо и вышел, заранее ёжась, из домика в рассветную прохладу."
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    window hide
    $ renpy.pause(2)
    scene bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_camp_center_day fadein 6
    window show
    "На улице оказалось даже холоднее, чем я думал."
    th "Надо было свитер прихватить."
    "Запоздало подумал я, шагая по дорожке и отчаянно зевая. Впрочем, не возвращаться же из-за него обратно."
    "Пытаясь согреться, я припустил трусцой по спящему пока ещё лагерю."
    "Рассудив, что спешка - отличный повод избежать ежедневного аттракциона с умыванием ледяной водой, я ограничился посещением гостепреимного домика с трафаретом «МЖ» на боковой стене."
    window hide
    scene bg ext_square_sunset with dissolve
    window show
    "Уже почти миновав площадь со сторожащим её Гендой, я случайно бросил взгляд в сторону главных ворот и увидел какую-то фигуру возле здания клубов."
    th "Кому это не спится в такую рань?"
    "Замедлив ход, я пригляделся. Судя по форменным шортам, это парень, но кто?"
    "Пионер тем временем воровато огляделся, сверкнув очками в лучах утреннего солнца, и исчез за кустами, растущими возле входа в клубы."
    th "Шурик? А он-то куда в такую рань поперся?"
    dreamgirl "Да в клуб, куда же ещё. Мысль приснилась. Изобретатель, что с него взять!"
    "На странности юного кибернетика мне было, по большому-то счёту, наплевать, так что я выбросил его из головы и заспешил дальше."
    window hide
    scene bg ext_houses_sunset with dissolve
    window show
    "Через несколько минут я уже шёл мимо последних домиков в дальнем конце лагеря."
    stop music fadeout 5
    "Дорожка здесь кончалась, но дальше в заборе действительно обнаружилась небольшая калитка, закрытая на засов без замка."
    jump alt_day5_uvao_road_to_old_camp
