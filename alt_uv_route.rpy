init:
    $ alt_day4_uv_viola_morning = False
    
    
label alt_day4_start_uvao:
    $ alt_chapter(4, u"Юля. Утро")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg int_house_of_mt_sunset
    window show
    "Проснулся я сам, спасая собственное сознание от какого-то дурацкого сна. Что-то про запчасти от когтистой перчатки… {w}Бред, короче. Впрочем, немудрено, после вчерашних-то событий."
    th "Так, будем рассуждать последовательно."
    th "Вчерашняя ушастая тень. Могла она мне привидеться?{w} Могла. Других свидетелей поблизости не было, подтвердить некому."
    dreamgirl "А я?"
    th "Если я привлеку тебя как свидетеля, это обеспечит мне путевку в веселый дом еще надежнее, чем кошастые галлюцинации."
    th "Как проверить, глючит меня или нет? Очевидное решение - наведаться к Виоле."
    dreamgirl "О йа-йа, доктор Виола пропишет тебе {i}процедуры{/i}, после которых тебя перестанут волновать воображаемые девочки!"
    "Я внутренне содрогнулся - воспоминания о манере Виолы проводить обследования были еще свежи."
    th "Какие еще варианты?"
    dreamgirl "Например, поспрашивать местных, вдруг они все в курсе про эту местную достопримечательность? Просто избегают про нее упоминать.{w} Почему-то."
    th "Может быть. Тут все может быть."
    play music music_list["my_daily_life"]
    "Я сел в кровати и принялся одеваться."
    "Скрипнула дверь, и в домик вошла Ольга Дмитриевна."
    show mt normal panama pioneer with dissolve
    mt "Семен? Уже проснулся?{w} Хорошо, умойся, причешись, и марш на линейку! Сегодня все должны примерно выглядеть.{w} Включая тебя!"
    me "А по какому поводу?"
    show mt angry panama pioneer with dissolve
    mt "Родительский день! Я же говорила вчера на линейке. Опять все мимо ушей пропускаешь?"
    me "А, ну да. Забыл."
    scene bg ext_house_of_mt_day with dissolve
    show mt normal panama pioneer with dissolve
    th "Родительский день, значит? Интересно, а что она ответит на это…"
    me "А мои родители не приехали?"
    mt "Приезжали рано с утра, оставили тебе мешок гостинцев, и уехали обратно."
    me "Мешок? А где он?"
    mt "В вожатской остался, не буду же я с ним по всему лагерю бегать! После обеда выдам, если хулиганить не будешь."
    mt "А вообще - хватит болтовни, давай бегом к умывальникам и на площадь!"
    th "Пожалуй, между линейкой и медпунктом я выберу медпункт."
    me "Ольга Дмитриевна, можно я сначала в медпункт загляну?"
    mt "А что такое?"
    show mt surprise panama pioneer with dissolve
    me "Да что-то странности какие-то со мной творятся, со вчерашнего дня. Видения…"
    mt "Ну-ка, давай выкладывай, что стряслось? Что еще за видения?"
    menu:
        "Рассказать про тень.":
            th "А почему бы и не рассказать? Закончится-то все равно отправкой к Виоле."
            me "Помните, у меня вчера живот прихватило?"
            show mt normal panama pioneer with dissolve
            mt "Конечно, помню. Как раз на мой танец!"
            dreamgirl "Ее это так цепляет? Пользуешься успехом, Семен! Но не ты ее танцевал, не тебе ее ужинать."
            me "Так вот, я потом увидел, что около столовой кто-то ходит.{w} Подошел поближе, думал, Алиса чем-нибудь поживиться решила."
            me "Смотрю – а там девочка незнакомая. {w}С кошачьими ушами и хвостом. Как-то так…"
            play music music_list["awakening_power"] fadein 0
            show mt angry panama pioneer with dissolve
            dreamgirl "Беги, Форест, беги! Судя по ее виду, тебя сейчас будут съедать заживо!"
            mt "Что за чушь? Семен, ты издеваешься?! Если решил прогулять линейку и зарядку таким образом – не выйдет!"
            mt "Или ты меня разыгрываешь, или тебя разыграли, а ты и рад поддаться!" 
            mt "Так, никакого медпункта, марш умываться! И чтобы я больше такой чепухи не слышала!"
            "Волной ее негодования меня просто снесло в направлении умывальников. А Ольга Дмитриевна с недовольным и озабоченным видом направилась в сторону площади."
            hide mt with dissolve
            stop music fadeout 5
            window hide
            jump alt_day4_uvao_morning_wash
            
        "Не рассказывать":
            "Что-то не нравится мне такой интерес к моим личным глюкам со стороны вожатой…  Отдаст еще потом в руки карательной психиатрии."
            "Виола в день моего появления показала себя гораздо более адекватным человеком в вопросах оценки состояния психики."
            me "Да так, в глазах периодически плывет… ну и в таком же духе. Наверное, действительно перегрелся."
            show mt normal panama pioneer with dissolve
            "Ольга Дмитриевна, услышав столь банальное пояснение, сразу потеряла интерес к деталям."
            mt "Тогда к Виоле загляни обязательно." 
            mt "На зарядку можешь не идти, а то такими темпами в медпункт тебя придется нести и до конца смены там и пропишешься."
            "Я кивнул и отправился к медпункту"
            hide mt with dissolve
            window hide
            jump alt_day4_uvao_aidpost
            
label alt_day4_uvao_morning_wash: #умываемся, беседуем с Элом про кошочку
    scene bg ext_houses_sunset with dissolve
    window show
    th "Может, действительно показалось?"
    dreamgirl "Ты знаешь, когда так кажется – тут уже и креститься бесполезно, друг мой."
    th "Ну или действительно разыграли…"
    dreamgirl "Кто, Алиска? Ты же ясно видел, фигура не та!{w} На ДваЧе не похоже, а остальные были на дискотеке… вроде бы.{w} Да и Ольга Дмитриевна как-то слишком уж взбеленилась на такую историю…"
    th "Но ведь получается как-то криво. Теория заговора и некодевочка из инкубатора? Пошло, заезженно и бывает только в аниме."
    window hide
    scene bg ext_washstand_day with dissolve
    window show
    "Я поймал себя на том, что уже давно дошел до умывальников и стою, сосредоточенно пялясь куда-то в сторону кустов." 
    "Остатки мыслей из головы выбило хлопком по плечу."
    show el smile pioneer with dissolve
    el "Чего стоишь, как будто рыжих высматриваешь? Они уже к площади идут, не бойся!"
    "Голос Электроника был настолько жизнерадостным и так контрастировал с моим утром, что хотелось его ударить."
    dreamgirl "Может, ты и ему расскажешь? Вдруг он видел, чьими стараниями тебе Ольга Дмитриевна против шерсти проехалась?"
    th "А почему бы и да? Хуже явно не будет. К тому же кошкодевочка – это не какой-нибудь многоцветный морфирующий конь."
    me "Да вожатая пропесочила…"
    me "Представляешь, я вчера около столовой во время дискотеки девочку увидел с кошачьими ушами и хвостом, думал, глюки.{w} Рассказал Ольге Дмитриевне, а она на меня вызверилась так, словно я ее лично оскорбил.{w} Вот теперь обтекаю."
    show el normal pioneer with dissolve
    el "Да, не повезло…{w} А вообще радуйся – легенду местную увидел."
    el "У меня друг позапрошлым летом тут отдыхал, рассказывал, что это что-то вроде местной лагерной легенды, мол, ходит иногда по лагерю девочка-кошка.{w} Сладости иногда ворует, другую мелочевку…" 
    el "Вроде даже ее кто-то видит периодически. Может, и ты сподобился.{w} Ну или действительно тебя разыграл кто-то, всякое бывает. Ты не скисай, главное!"
    "Я угрюмо кивнул и направился к умывальнику. Пытка холодной водой – действо неприятное, но неминуемое."
    hide el with dissolve
    play sound sfx_open_water_sink
    $ renpy.pause(1)
    play sound_loop sfx_water_sink_stream
    "От холодной воды ломило челюсть, руки немного онемели, но настроение явно стало лучше, да и спать уже не хотелось. Теперь надо бы держать курс на площадь, а то вожатая с меня три шкуры спустит."
    stop sound_loop
    window hide
#    scene bg ext_square_sunset with dissolve
    scene cg d2_lineup
    window show
    "Линейка и зарядка прошли в уже привычном ключе."
    "Славя оправдывала свой статус помощницы вожатой на все сто, остальные с разной периодичностью зевали и поглядывали в сторону столовой."
    play music eat_horn fadein 3
    "Вот и долгожданные звуки горна!"
    stop music fadeout 5
    window hide
    jump alt_day4_uvao_breakfast

label alt_day4_uvao_aidpost: #беседуем с Виолой
    scene bg ext_square_sunset with dissolve
    window show
    $ renpy.pause(1)
    window hide
    scene bg ext_aidpost_day with dissolve
    window show
    stop music
    play sound sfx_knock_door7_polite
    $ renpy.pause(2)
    cs "Да-да, войдите!"
    "Я поежился, вспомнив  предыдущую встречу с медсестрой, но отступать было некуда."
    window hide
    scene bg int_aidpost_day with dissolve
    window show
    show cs normal with dspr
    me " Виолетта Церновна, а я к вам с проблемой."
    play music music_list["eternal_longing"] fadein 5
    show cs smile with dspr
    cs " Просто Виола, пионер, для тебя – просто Виола…"
    dreamgirl "Если ты к ней по делу – не красней и взгляд подними выше выреза на халате, дубина! Иначе твое дело ширинку скоро рвать начнет!"
    "Я собрался с мыслями и начал объяснять."
    me "Эм-м-м… Тут так получилось… Вопрос достаточно деликатный…"
    show cs grin with dspr
    cs "В ящике стола, бери, сколько надо."
    "Под взглядом медсестры я подошел к столу, открыл ящик и увидел горку квадратных пакетиков с надписью «Изделие №2». Лицо Виолы выражало исключительно дружелюбное участие."
    show cs normal with dspr
    me "Нет-нет, не в этом дело! Я… Мне… В общем, у меня, судя по всему, галлюцинации!"
    cs "Ну, ты сам пришел и сказал, значит, не все еще потеряно. И что же тебе мерещилось?"
    me "Ну, вчера во время дискотеки мне живот прихватило, я и ушел…{w} А потом увидел, что около столовой тень какая-то, думал, Алиса шастает, присмотрелся – а у нее уши кошачьи. И хвост.{w} У тени, а не у Алисы, Алисы там вообще не было.{w} Я подумал — нарядился кто-то, а оно ухом дёрнуло.{w} Вот."
    th "Идиот. Полный и беспросветный. Сейчас тебя накормят галоперидолом, потом воткнут в задницу шприц с аминазином, чтобы не особо дергался, и отправят в комнату с мягкими стенами."
    "Как ни странно, Виола не выказывала никакой тревоги и волнения, скорее на ее лице читался вполне себе явный интерес."
    stop music fadeout 5
    cs "Девочку-кошку? Не ты первый, пионер, не ты последний… В твоем возрасте это нормально, фантазии и не такие бывают…{w} но в данном случае ты столкнулся с настоящей легендой. Не знаю, почему Ольга…"
    me "А при чем здесь Ольга Дмитриевна?"
    cs "Когда она в «Совенке» работать начала, эта легенда только появилась. Ей её подопечные все уши прожужжать успели, теперь из-за каждого упоминания бесится. А потом как-то поутихли слухи понемногу."
    me "И давно вы тут? А что за легенда?"
    show cs shy with dspr
    cs "Пионер, посмотри на меня внимательно и подумай, насколько невежлив был твой первый вопрос. Я выгляжу настолько старой, чтобы это было давно?"
    "Я нечленораздельно квакнул и отрицательно мотнул головой."
    show cs normal with dspr
    cs "То-то же. А легенды как таковой нет, просто начали рассказывать, что видели девочку с кошачьими ушами и хвостом. Еще периодически из столовой всякая всячина пропадает, но тут уж скорее пионеры под шумок действуют.{w} Так говоришь, где ты ее видел?"
    me "Около столовой…"
    cs "И ты уверен, что это не Алиса была?"
    me "Не, там фигура… Не Алиса, короче."
    "В глазах Виолы блеснул интерес."
    cs "Знаешь, пионер… Ты смотри, если еще где-нибудь заметишь – заходи, рассказывай, я буду очень благодарна."
    $ alt_day4_uv_viola_morning = True
    "Последние слова в исполнении Виолы чисто автоматически трактовались весьма интересным, но несбыточным образом. В горле снова пересохло, но в этот раз я сумел перебороть себя."
    me "Надеюсь, благодарность будет выражена… интересным образом."
    dreamgirl "Так держать! Еще бы на полтона ниже – и звучало бы уже совсем намеком!"
    show cs smile with dspr
    cs "А ты весьма неплохо держишься… для школьника."
    play music eat_horn fadein 3
    "Нашу беседу прервал горн. Виола направилась к двери."
    cs "Завтракать идешь, пионер? Ольге я скажу, что ты в полном порядке."
    "Я кивнул и направился к столовой."
    hide cs with dissolve
    window hide
    stop music fadeout 5
    jump alt_day4_uvao_breakfast

label alt_day4_uvao_breakfast:
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_sunset  with fade
    window show
    "Свободных мест в столовой, как всегда, не хватало." 
    "Детальный осмотр местности показал, что сесть я могу либо с рыжим дуэтом, от близости с которым всех предостерегал здравый смысл, либо с нашей доблестной девочкой-пулеметом восточного происхождения."
    dreamgirl "Ну что, путь смертника или путь стоика?"
    th "Лучше путь стоика. Мне как раз надо крепко обдумать пару вопросов, под болтовню это явно проще, чем под риск съесть кого-нибудь не того."
    show mi normal pioneer with dspr
    "Я сел рядом с Мику, улыбнулся и начал разбираться с содержимым тарелки. Она что-то тараторила, я кивал и погружался все глубже в размышления.{w} Вернее, в пустоту, из которой должны были родиться хоть какие-то мысли."
    th "Я тут уже четвертый день, а все еще забиваю на самые важные вопросы.{w} Для начала – текущая дата, местоположение лагеря и памятник на площади, при первом же вопросе о котором Лена  только что не отпрыгнула."
    dreamgirl "Может, она тебя за начинающего пикап-мастера приняла. Мол, начал тут один шаблоны рвать. А они-с барышни стеснительные и таких подкатов не понимают, у них Митчелл и романтика."
    th "Ша, о важном думать надо. На реконструкцию это не тянет – не поверю, что столько народа так старательно будут косить под пионерлагерь и добровольно откажутся от своих девайсов."
    th "Да и как я в таком случае здесь оказался? К тому же из зимы в лето…{w} Вариантов всего два – путешествие во времени и путешествие в параллельный мир.{w} И в том, и в другом случае, раз меня не встречают с цветами или наручниками, разгребаться придется самому."
    show mi serious pioneer with dspr
    "Я заметил, что Мику встревоженно смотрит на меня, и только тогда обнаружил, что в очередной раз подношу ко рту пустую ложку."
    me "Извини, задумался!"
    show mi smile pioneer with dspr
    "Мику рассмеялась с облегчением."
    mi "Ну, Сёма, ты даешь, так задуматься. Я уж думала, тарелку процарапаешь или ложку съешь! А о чем ты таком задумался? Не выспался, что ли?{w} Я вот если не высплюсь, тоже могу вот так вот задуматься, почти сплю тогда на ходу даже. Или что-то случилось?"
    mi "Ой, ты знаешь, Шурик вчера с крыши упал, ушибся сильно, в медпункте лежит. Но вроде бы ничего страшного.{w} А к тебе сегодня родители приедут?" 
    "Очередной поток болтовни практически смыл все попытки определиться с планом действий. Я отрицательно мотнул головой на ее расспросы и молча отправился в сторону выхода."
    mi "… заходи в клуб, если что! Вдруг скучно будет!"
    "догнал меня голос Мику."
    hide mi with dspr
    stop ambience
    window hide
    scene bg ext_dining_hall_near_day
    window show
    th "Где разжиться более-менее актуальной информацией о происходящем, не вызывая подозрений?{w} Правильно, в интернете. Чем заменить при отсутствии?{w} Телевидением и газетами."
    th "Насчет ти-ви не знаю, а вот газеты… Надо бы наведаться в библиотеку."
    dreamgirl "Ну наконец-то ты пошевелил мозгами хоть как-то.{w} Попроси подшивку журналов каких-нибудь, энциклопедию, что-нибудь еще…"
    th "А ведь действительно! Попрошу, к примеру, прошлогоднего «Юного техника» - вот и год вычислил, и не спалился. Да и вообще.{w} Только Жужелица…"
    dreamgirl "А ты ее палкой по голове тюкни – она мешать и не будет.{w} Можешь даже воспользоваться беспомощностью девушки в своих мерзких целях, разрешаю. Нарисовать на ней что-нибудь, например…"
    "Разговаривая с шизой, я перестал следить за дорогой и буквально врезался в Ольгу Дмитриевну."
    
