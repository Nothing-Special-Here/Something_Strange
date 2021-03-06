# Хозработы (Со Славей). Палевная Ветка
#
# Используется флаг alt_uvao_D5_sh_mines
#
label alt_day6_uvao_duty_sl:
    window hide
    $ alt_chapter(6, u"Юля. Хозработы")
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    play music music_list["get_to_know_me_better"] fadein 4
    #REMOVE THIS!
    $ persistent.sprite_time = "day"
    $ day_time()
    #REMOVE THIS!
    window show
    "Славя уже была на месте и подметала площадку возле Генды. Вот ведь деятельная девочка! Не зря её вожатая своим заместителем назначила."
    dreamgirl "Само собой. Кто-то ведь в лагере должен работать. А Ольге Ленивовне недосуг. Она занята - ленится."
    "Я бы тоже не отказался сейчас сесть на скамеечку в тенёчке и предаться блаженной праздности. Но обещал ведь помочь, значит надо выполнять обещание."
    show sl normal pioneer far at center with dissolve
    "Я невольно залюбовался Славей, чуть не танцующей с метёлкой в руках. Как у неё ловко всё выходит. А подойдя поближе, ещё и услышал как она напевает какую-то мелодию."
    sl "…ах, какое блаженство, знать, что ты совершенство, знать, что ты идеал…"
    me "Привет ещё раз, Славя. Что это ты такое поёшь?"
    show sl smile pioneer at center with dissolve
    "Славя заметила меня и заулыбалась."
    sl "А, это из фильма одного. Про Леди Совершенство."
    me "Про тебя значит?"
    show sl shy pioneer with dspr
    "Не смог сдержать улыбки и я."
    sl "Ну что ты!"
    "Отмахнулась она, хотя я видел, что ей явно было приятно."
    sl "Какое я совершенство? Я обычная пионерка."
    "Решив оставить на потом размышления о совершенствах и пионерках, я спросил:"
    show sl smile pioneer with dspr
    me "Слушай, Славь."
    sl "Да, Сёма?"
    me "Всё-таки, почему ты решила обратиться именно ко мне? Я ведь мог и отказаться."
    show sl laugh pioneer with dspr
    sl "На самом деле нет, не мог."
    "Рассмеялась девочка."
    "А я удивлённо поднял бровь. Как это понимать – \"не мог отказаться\"? Лагерь всё-таки не исправительный, а пионерский. Или она имеет ввиду что-то другое?"
    show sl smile pioneer with dspr
    sl "На самом деле, меня Ольга Дмитриевна к тебе направила."
    "Решила не томить меня неведением Славя."
    sl "Сказала, что ты на весь день поступаешь в моё личное распоряжение по хозяйственной части."
    "Ах вот оно что..  Видимо Славя заметила тень разочарования, мелькнувшую на моём лице, поэтому решила подсластить пилюлю."
    sl "Но я обратилась бы к тебе в любом случае. Мне хотелось бы, чтобы мне помогал именно ты. И я не хотела без лишней необходимости применять эту крайнюю меру принуждения."
    show sl shy pioneer with dspr
    sl "Я знала, что ты не откажешь мне, Сёма."
    "И она снова улыбнулась."
    show sl smile pioneer with dspr
    sl "А теперь, когда мы всё выяснили, давай начнём работать."
    hide sl with dissolve
    "Она скрылась  за постаментом  памятника и вышла оттуда со второй метлой в руках."
    show sl normal pioneer with dissolve
    sl "Вот, бери метлу, давай уберём площадь. Это не займёт много времени."
    "Я оглядел площадь. Ну да, конечно."
    "И внезапно вспомнил, что кого-то здесь явно не хватает."
    me "Так, а Электроник где? Помнится, у тебя ещё один помощник должен быть."
    sl "А он на сцене - проверяет электропроводку. Для подключения аппаратуры."
    me "Аппаратуры?"
    sl "Ну да, из музыкального клуба. Концерт же будет, забыл что-ли?"
    sl "Мы тут сейчас быстренько подметём и сразу туда. Он к этому времени тоже как раз должен закончить."
    window hide
    hide sl with dissolve
    window show
    "Ну быстро - не быстро, а примерно полчаса времени пришлось потратить на подметание. Мусора на площади было хоть отбавляй - нерадивые пионеры постарались. Вот их бы сейчас и заставить убираться."
    me "Что теперь? Садимся на мётлы -  и вперёд, на сцену?"
    show sl laugh pioneer at center with dissolve
    "Славя снова рассмеялась моей шутке."
    dreamgirl "Да ты сегодня в ударе, гусар."
    sl "Мётлы  можно пока здесь оставить, я их вечером отнесу в подсобку. А мы с тобой сразу в клуб пойдём. Электроник нас уже, наверное, заждался."
    sl "Я ему сказала, чтобы через полчаса был как штык возле музыкального клуба. А он очень ответственный, будет волноваться ещё."
    hide sl with dissolve
    "И оставив мётлы около памятника Генды, мы отправились к музыкальному клубу."
    window hide
    scene bg ext_musclub_day
    show sl normal pioneer
    with dissolve
    window show
    "Но возле клуба Электроника не было."
    th "Где же наш невероятно пунктуальный кибернетик?"
    el "Ребята! Вот вы где!"
    "Раздался сзади запыхавшийся голос Сыроежкина."
    show sl normal pioneer at right
    show el normal pioneer at left
    with dissolve
    el "Слушайте, где вы ходите? Я вас по всему лагерю ищу бегаю… Работа же стоит."
    "Сам того не подозревая, Электроник процитировал фразу из очень известного фильма."
    me "Работа стоит, а срок идёт. Не забывай: у тебя зарплата в рублях, а у меня в сутках."
    "В тон ему ответил я."
    show sl laugh pioneer at right
    show el laugh pioneer at left
    with dissolve
    "Все рассмеялись."
    show sl normal pioneer at right
    show el normal pioneer at left
    with dissolve
    sl "Ладно, заходим, а то и правда не успеем ничего."
    window hide


    #ЛБ: хорошо бы поставить какую-нибудь мелодию на фортепьяно, раз Мику репетирует. Например, memories_piano. Потом мелодия обрывается по короткому fadeout после реплики Мику
    #К: Поставил, что нашёл
    play ambience ambience_music_club_day fadein 4
    play music lastlight_piano fadein 2
    scene bg int_musclub_day with dissolve
    window show
    "В этот раз Мику не сидела под роялем, а вполне себе репетировала какую-то песню. Наверное репертуар на вечер подбирает."
    show mi normal pioneer at right behind sl
    show sl normal pioneer
    show el normal pioneer at left
    with dissolve
    stop music fadeout 1
    play sound sfx_piano_head_bump
    mi "Привет, ребята! Как хорошо, что вы зашли."
    "Защебетала болтушка и махнула головой, отчего длиннющие ультрамариновые хвосты её волос прыгнули вверх-вниз. Я невольно залюбовался."
    show mi happy pioneer at right with dspr
    mi "Я столько всего приготовила к концерту! Буду петь, и танцевать, и вести… А вы что-нибудь приготовили?"
    if alt_day2_club_join_musc:
        "Я отрицательно помотал головой и Мику укоризненно посмотрела на меня."
        mi "Сёма, ты ведь записывался в музкружок, а не участвуешь ни в каком номере. И даже ни разу не зашёл на одну репетицию. Не стыдно тебе?"
        "Я пожал плечами."
        me "Да не особенно…"
        "Мику изо всех сил старалась напустить на себя строгий вид, но глаза её смеялись."
        mi "Ладно, мы ещё сделаем из тебя настоящего музыканта. Ещё будешь выступать…"
    sl "Подожди, Мику."
    show mi normal pioneer at right with dspr
    "Остановила девочку-оркестр Славя."
    sl "Нам нужны инструменты и аппаратура."
    mi "Конечно-конечно, берите. Вот гитары, вот барабанная установка, вот усилитель, а вот здесь колонки."
    "Говорила она, показывая на озвученные предметы."
    mi "А вот шнуры ещё. И стойки для микрофонов."
    "Я почесал затылок, оглядывая всё это музыкальное добро. Много. За один раз-то и не унести. Но уж взялся за гуж…"
    "И вот уже второй раз мы с Электроником стали товарищами по несчастью в переноске всяких тяжёлых и бесполезных грузов."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_stage_normal_day
    with dissolve
    window show
    "Проклятый усилитель оттянул мне все руки, а несчастные две сотни метров от клуба до сцены показались марафонской дистанцией. Почему здесь так распространён ручной труд? Надо в следующий раз какую-нибудь тачку приспособить."
    "Мы занесли деревянного монстра по ступенькам и с усилием поставили на дощатый пол сцены. Так, самое сложное позади. Правда, своей очереди на переноску ожидают четыре колонки, но они явно весят меньше, чем усилок." #ЛБ: с облегчением поставили. Или с усилием, но подняли. Или кое-как сгрузили. Кстати, колонки, про которые речь - реально крупные и вовсе не лёгкие, судя по тексту Автора, и какими я лично помню подобные в те времена.
    "Провозившись пару часов, мы наконец перенесли всё. Хорошо, что девочки помогали. Да, Мику тоже не смогла усидеть в клубе, и под предлогом «мне тут одной всё равно скучно», вместе со Славей носила то, что полегче."
    play music eat_horn fadein 3
    "Тем не менее, все устали и с облегчением вздохнули, когда раздался сигнал горна, призывающий пионеров на обед." #ЛБ: "все устали и с облегчением вздохнули". Необходимо разбить, например "...здорово устали, так что с облегчением вздохнули..."
    stop music fadeout 5
    # TODO: Не забудь поменять точку входа
    jump alt_day6_uvao_lunch

# Хозработы. Беспалевная Ветка
#
# Используется флаг alt_uvao_D5_sh_mines
#
label alt_day6_uvao_duty:
    window hide
    $ alt_chapter(6, u"Юля. Хозработы")
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    play music music_list["went_fishing_caught_a_girl"] fadein 4
    #REMOVE THIS!
    $ persistent.sprite_time = "day"
    $ day_time()
    #REMOVE THIS!
    window show


    "Сразу же за дверями столовой меня окликнули."
    show mt pioneer normal veryfar:
        zoom 0.8 xalign 0.5 yalign 1.0
    show el normal pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    el "Семён! Ну что, ты готов?"
    me "Нет. Мне надо принять ванну и выпить чашечку кофе."
    "Они оба фыркнули."
    el "И ванна, и кофе, и какава с чаем. Все после работы."
    me "А чего делать-то надо?"
    el "Как что? Сейчас сначала провода прозвоним - там, похоже, где-то обрыв - заменим-починим что найдём, а потом аппаратуру подключать будем."
    el "Ну и вообще, прибрать там всё, в порядок привести."
    el "Пошли!"
    "И мы пошли."
    hide mt
    scene bg ext_square_day
    show el normal pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    el "Эй, ты куда? "
    me "К сцене, куда ж ещё?"
    el "А инструменты? Надо из клуба взять."
    "Вздохнув, я - уже на полпути к сцене - развернулся и двинулся вслед за нашими гениями-ремонтниками."
    scene bg ext_clubs_day 
    show el normal pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    hide el with moveoutleft
    "Кстати."
    me "Шурик, тебя же, вроде как, освободили?"
    sh "Да. Освободили."
    "Радости в его ответе заметно не было."
    me "Так зачем ты тогда с нами идёшь?"
    sh "Да я так, за компанию."
    show el normal pioneer far at cleft with dissolve
    "Электроник тем временем выволок на улицу памятную стремянку, а потом и внушительный портфель с инструментами."
    el "Что возьмешь?"
    me "Лестницу. "
    th "Она хоть и громоздкая, но вроде полегче. Он что, решил с собой взять всё, вплоть до токарного станка?"
    sh "Ребят, ну давайте я помогу?"
    el "Нет, тебе нельзя. Доктор запретил."
    sh "Ну-у…"
    el "Нет! Она и мне специально сказала, чтоб я тебе не позволял напрягаться. Так что…" 
    el "Иди лучше отдохни. На пляж сходи, книжку почитай. А мы справимся."

    scene bg ext_square_day 
    show el normal pioneer
    with dissolve
    "Мы оставили печального гения горевать в одиночестве и потащились обратно. Треклятая лестница впивалась углами мне в бок, да и напарник мой то и дело перекладывал чемодан из одной руки в другую."
    if alt_uvao_D5_sh_mines:
        "Вчера таскать, сегодня таскать… Нашли верблюда, блин!"


    scene bg ext_stage_normal_day 
    show el normal pioneer
    with dissolve
    play sound sfx_metal_door_large_close_basement
    me "Фух. Всё!!!"
##металлический бамц
    "Я сбросил ненавистный груз и с наслаждением растянулся не скамейке. Электроник уселся на соседней и сложил руки на коленях."
    el "Уф. Еле дотащил!"
    me "А нафига ты столько взял?"
    el "Ну как зачем, мало ли что делать придётся? А тут у меня и молоток, и стамеска, и отвёртки, и паяльник, и гвозди-шурупы всякие…"
    me "Да? Ну-ну…"
    "Я почему-то не чувствовал никакого трудового энтузиазма. Поскорей бы уже разделаться и удрать."

    el "Ну что, начнём?"
    el "Надо сначала кабели проверить, там какие-то, похоже, перебиты…"
    me "Я так понимаю, на лестницу опять мне лезть?"
    el "Ага… Но ты не волнуйся, я тут внизу все беру на себя! Тебе только кабель снять и потом обратно повесить."
    me "А какой именно? Их тут десяток всяких разных!"
    el "А… а щас мы их прозвоним!"
    "Он водрузил свой чемодан на сцену, и, покопавшись в нем, стал доставать оттуда какие-то запчасти. Провода, батарейку, какие-то мелкие детали…"
    dreamgirl "Паспарту, достань из саквояжа ложку, кувалду, велосипед и орбитальный лазер."
    el "Вот! Готово!"
    "Он торжествующе продемонстрировал своё творение, похожее на… типичное изобретение безумного учёного."
    el "Сейчас мы их прозвоним… ага… ага… ага!"
    "Пока он там возился с проводами, я сел на край сцены и бездумно уставился в небо. Не хотелось ничего - ни выяснять, как я попал сюда, ни допытываться до остальных тайн… Сейчас закончим с этими чертовыми проводами, и отправлюсь искать Юлю."

    el "Семён! Я нашёл!"
    "В руке он держал пару хвостов, уходящих куда-то вверх."
    el "Надо их снять, найти обрыв, и соединить обратно. А, ну и повесить обратно."
    me "А может, просто новые протянем?"
    el "Да, понимаешь… нету новых. Закончились."
    th "Ага. Небось, извели всё на свои прожекты… Робота своего."
    el "Да они нормальные, я спаяю, не хуже новых будут! Ты только сними. И потом повесь."

    "Мне уже надоело с ним препираться, и я выволок стремянку на сцену."
    el "Подержать?"
    me "Не надо. Лучше дай отвертку. Плоскую."

    "Провода, по советской манере закрепленные гнутыми гвоздиками, постепенно перемещались на досчатый пол, где подвергались пристальному изучению на предмет разрывов." 

    el "Ага! Вот где!"
    "Издал Сыроежкин торжествующий крик и схватился за паяльник."
    el "Сейчас тебя починим… сейчас-сейчас… сейчас."

    "Я продолжал методично отгибать гвоздики и освобождать провода. Гений-ремонтник, на четвереньках и с высунутым языком, увлеченно сращивал жилы. Змеиное шипение и едкий запах канифоли, дымящий паяльник…"
    th "Я в аду, мама."
    dreamgirl "Ты излишне драматизируешь, тебе не кажется?"
    th "Не кажется. Я в этом уверен."

    show sl smile pioneer at right with dissolve
    sl "Привет, Семён! Как успехи?"
    el "Почти готово! Останется только заново провода закрепить - и всё."

    sl "Наверное, лучше сначала усилитель принести. Поможешь… поможете? А потом я помогу провода убрать."
    "Почему-то она обращалась исключительно ко мне. Закопавшийся в груде проводов Сыроежкин удостоился только мимолетного взгляда."
    el "Конечно, поможем! Так ведь, Семён?"
    th "А вот он, похоже, наоборот старается обратить на себя внимание."
    me "Ага."
    "Я отставил лестницу и спрыгнул со сцены, и мы двинулись к музыкальному клубу."

#копипаста из нынешних хозработ:
    play ambience ambience_music_club_day fadein 4
    play music lastlight_piano fadein 2
    scene bg int_musclub_day with dissolve
    window show
    show mi normal pioneer at right behind sl
    show sl normal pioneer
    show el normal pioneer at left
    with dissolve
    "В этот раз Мику не сидела под роялем, а вполне себе репетировала какую-то песню. Наверное репертуар на вечер подбирает."
    stop music fadeout 1
    play sound sfx_piano_head_bump
    mi "Привет, ребята! Как хорошо, что вы зашли."
    "Защебетала болтушка и махнула головой, отчего длиннющие ультрамариновые хвосты её волос прыгнули вверх-вниз. Я невольно залюбовался."
    show mi happy pioneer at right with dspr
    mi "А мне Ольга Дмитриевна уже всё рассказала. Вечером будет концерт. Художественная самодеятельность." #ЛБ: можно предположить, что худрук музкружка об этом знала за пару недель - как минимум (что подтверждается, например, Лена и Алиса-рутами)
    "И Мику от удовольствия зажмурилась."
    mi "Я буду играть и петь. Я много на чем умею играть, честно-честно. На гитаре, на барабанах и на флейте ещё." #ЛБ: про мультиинструментализм - уже было в Д2. Или надо мысленно отметить, что повторяется, тараторка эдакая
    mi "И другие ребята будут играть. А ты, Сёмочка, играешь на чём-нибудь? А ты, Сыроежкин?" #ЛБ: см. выше - про умения Сэма аналогично
    sl "Подожди, Мику."
    show mi normal pioneer at right with dspr
    "Остановила девочку-оркестр Славя."
    sl "Нам нужны инструменты и аппаратура."
    mi "Конечно-конечно, берите. Вот гитары, вот барабанная установка, вот усилитель, а вот здесь колонки."
    "Говорила она, показывая на озвученные предметы."
    mi "А вот шнуры ещё. И стойки для микрофонов."
    "Я почесал затылок, оглядывая всё это музыкальное добро. Много. За один раз-то и не унести. Но уж взялся за гуж…"
    "И вот уже второй раз мы с Электроником стали товарищами по несчастью в переноске всяких тяжёлых и бесполезных грузов."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_stage_normal_day
    with dissolve
    window show
    "Проклятый усилитель оттянул мне все руки, а несчастные две сотни метров от клуба до сцены показались марафонской дистанцией. Почему здесь так распространён ручной труд? Мы занесли деревянного монстра по ступенькам и с усилием поставили на дощатый пол сцены." #ЛБ: см. примечание к предудущему клону
    show el normal pioneer at right
    show sl normal pioneer
    with dissolve
    "Я присел на край сцены, тяжело дыша. Болели руки. Электроник пристроился рядом. С меня градом лил пот. По лицу кибернетика было видно, что он чувствует себя не лучше. А ведь ещё четыре колонки, каждая из которых весит как половина усилителя ждали своего часа…"
    me "Передохнём пару минут."
    "Предложил я."
    el "Ага."

    "Мы повалились на зрительские скамейки. "
    sl "Устал, Семён?"
    me "Угу. Есть такое. "
    sl "Бедный… Еще немного осталось. Зато концерт будет на пять с плюсом, и танцы потом! Ты ведь пойдёшь на танцы?"
    "Я неопределенно хмыкнул и пожал плечами."
    el "Кстати, Славя… Славя?"
    sl "Обязательно приходи! Я буду ждать!"
    el "Славя!"
    "Электроник попытался еще раз привлечь ее внимание."
    show sl angry pioneer with dspr
    sl "Чего тебе, Сыроежкин?!"
    el "А… Ты не знаешь, Женя на танцы пойдёт?"
    sl "Не знаю! Пойди сам у неё спроси, если так интересно!"
    th "Вот тебе и добрая отзывчивая Славя…"
    me "Может, пойдем остальное притащим? Я вроде отдохнул, а ты?"
    show sl normal pioneer with dspr
    "Я попытался нейтрализовать непонятно из-за чего разгорающийся конфликт. В конце концов, чем дольше они цапаются, тем дальше отодвигаются поиски Юли..."
    el "Да, пойдём."

    "С колонками дело прошло легче. Мы в быстром темпе сбегали  четыре раза туда-сюда, оставив всякую неудобную мелочевку на попечение Слави, и вскоре колонки заняли свое место по углам сцены."

    sl "Давай я провода обратно закреплю. Ты устал, наверное? Я все сделаю."
    show sl shy pioneer with dspr
    sl "Только… можешь лестницу подержать? "
    sl "Просто на всякий случай."
    show sl normal pioneer with dspr
    th "Если она высоты боится - зачем тогда лезет? Да еще так настырно."
    th "Что ей от меня надо?!"
    dreamgirl "Да кто ж её, кобылу, знает. Может, спросить?"
    th "Нет уж. Давай я просто закончу с этими чертовыми проводами - и всё!"

    "Я установил стремянку понадежнее, и Славя, цепляясь за перекладины, взобралась наверх."
    show sl scared pioneer with dspr
##ракетный старт Слави. Был такой спрайт
    sl "Семён! Только держи! Держи, пожалуйста!"
    me "Да держу, держу."
    "Пробурчал я, крепко вцепившись в стойки."
    th "Сами бы управились, чего ей втемяшилось помогать? Будто дел больше нет."
    dreamgirl "Ну, нет худа без добра. Ты уже заценил, какие ножки?"
    dreamgirl "Загорелые, спортивные, в белых носочках. Мечта!"
    "Я и сам против воли осязал легкое тепло, исходящее от гладкой кожи, и едва уловимый аромат. Дурацкая мысль - коснуться не руками, не губами, лишь одним теплым дыханием, под коленкой…"
    if alt_uvao_D5_hentai:
        th "Стоп, стоп, очнись! Только вчера с Юлей валялся, а теперь на активистку заглядываешься?"
        dreamgirl "Думаешь, твоя кошечка знает, что такое ревность? Сомневаюсь."
    else:
        th "Так, стоп. Отставить разврат! Мне сейчас не до этого."
    dreamgirl "А если ещё вверх взглянуть… Видно, конечно, не очень, но кое-что разглядеть можно!"
    $ renpy.pause(1)
    show sl smile pioneer with dissolve
    dreamgirl "Шухер!"
    "Я не успел отвести глаза и встретился взглядом со Славей. Она смотрела на меня сверху и… улыбалась. Понимающе и чуть-чуть торжествующе."
    th "Она это специально? Вылезла покрасоваться!"
    th "А чего это я смущаюсь, как школьник какой-то?! Мне показывают, я пялюсь. Какие-то проблемы?"
    "Я преодолел желание отвернуться и нагло, с вызовом встретил ее взгляд. Ну, и что дальше будешь делать?"
    "Мы играли в гляделки целую вечность - секунд десять, не меньше. Славя, вдруг закусив губу, нервно скомкала юбку на бедре и едва заметно потянула выше."
    th "Она что, собирается тут стриптиз устроить?!"
    dreamgirl "Ты против?"
    th "Но… блин, мы же тут не одни! Электроник вон сидит! Неужели ей настолько на него  наплевать?"


    us "Эй! Семён! Тебя ОльДмитревна зовёт!"
    "Крайне вовремя выскочившая из зарослей Ульяна спасла меня. По крайней мере, дала уважительный повод разорвать контакт."
    me "А зачем?"
    us "Не сказала! Сказала только тебя позвать, чтоб ты к ней шёл."
    "Отработав свою роль гонца, мелкая снова скрылась в кустах, пока её тоже не припахали к общественной работе. Надо бы и мне воспользоваться шансом."
    me "Ну, я пошёл тогда. Вожатая зовёт!"
    "Не дожидаясь ответа, я спрыгнул со сцены и поскорее отправился по тропинке в сторону домиков."

    if not alt_uvao_D5_sh_mines:
        menu:
            "Забить на всё и пойти к Юле":
                jump alt_day6_uvao_fuckoff_mt
            "Поверить Ульяне":
                jump alt_day6_uvao_isolator_house
    else:
        jump alt_day6_uvao_isolator_house
