label alt_day5_uv_bunker:
    $ routetag = "uv"
    $ alt_chapter(5, u"Юля. Бункер")
    $ persistent.sprite_time = "day"
    $ day_time()
    
    #Hentai
    $ alt_day5_uv_hentai = False
    
    scene bg int_catacombs_door
    play music music_list["orchid"] # Вообще его вставить надо по приходу в бункер \ лагерь. Мы же тут первый раз.
    
    me "Ого, мощно сделано. Интересно, что там, за этой дверью?"
    uv "Не знаю. У меня не получалось открыть."
    "Я попробовал повернуть колесо, но - увы, сил не хватало."
    "Немного пошаря глазами по сторонам я нашёл какую-то железяку."
    th "Хмм, а что если?..."
    "Подобраю свою находку я вставил её в колесо."
    me "Дайте мне точку опоры, иииии..."
    "И нихрена. Я надавил еще сильнее, потом пнул арматурину коленом, надеясь таки сдвинуть заржавевший механизм. Это было опрометчиво."
    me "Аййй!"
    dreamgirl "Сила есть - ум не поможет."
    "При ударе я похоже не расчитал силу, в следствии чего моё правое колено немного взвыло."
    me "Попытка номер два."
    "Я вцепился в железяку и повис на ней всем своим весом."
    "Раздался жуткий скрежет, и затвор стронулся с места. Юля от неожиданности отпрыгнула на пару метров и уставилась на дверь."
    show uv surprise at center with dissolve
    uv "Скрипит. Получилось?"
    "Я довернул затвор до конца и потянул. Дверь очень неторопливо провернулась на петлях."
    me "Похоже что да."
    
    scene bg int_catacombs_living
    show uv surprise at center with dissolve
    play music music_list["waltz_of_doubts"]
    
    "За дверью оказалось убежище, в его классическом виде. Двухъярусная кровать, какие-то приборы - работающие, что удивительно! - шкафчики с какими-то ящиками. Похоже, именно сюда стремился Шурик."
    "Правое колено начинало выть всё сильнее, и я, стараясь не беспокоить его, допрыгал до кровати на левой ноге."
    me "Подожди, давай передохнём. Я похоже сильно ногу ушиб, и не смогу идти какое-то время."
    uv "Хорошо, давай."
    "Я решил посмотреть, что с ногой и закатал штанину. На коленке красовалась небольшая ссадина."
    uv "Залижи."
    me "A?"
    uv "Залижи. Я всегда так делаю. Мне очень помогает."
    
    show uv smile at center with dissolve
    
    "Она задрала ногу и продемонстрировала, кося на меня желтым глазом."
    
    "Я усмехнулся. Ну и кошка!"
    dreamgirl "Может она и тебе коленку полижет, вдруг пройдёт?"
    "Шиза была как всегда в своём репертуаре."
    th "Отвали, не до этого сейчас."
    me "Не, мы так не делаем."
    "С некой гордостью сказал я."
    me "Мне бы немного льда. Да только где его тут взять?"
    uv "Вот поэтому зализывать лучше."
    "Но тут с ней не поспоришь. В лагере это не составило бы труда, но вот в атомном убежище лёд найти не такая уж и лёгкая задача."
    "Вставать с кровати не хотелось. Слишком рано встал, слишком много беготни по лесам, руинам и туннелям, а также бесед с этим...существом, Юлей."
    "Должно быть, именно так себя чувствует чересчур разогнанный комп во время серьёзных вычислений - мой мозг практически кипел. Я вытянулся на кровати и закрыл глаза."
    "Толчок в плечо."
    uv "Дверь закрой. А то этот, друг твой, нас найдёт."
    me "И не друг он мне вовсе!"
    "Возмутился я."
    "Но в целом - она была права, тут же ещё Шурик шляется где-то. Не хватало ещё что-бы он меня нашёл в ядерном убежище с девочкой, которая помимо хорошей фигуры имеет пару кошачих ушей и хвост."
    "Застонав, я поднялся, допрыгал на одной ноге до двери, закрыл её и свалился на кровать. А теперь - спать! Последнее что я почувствовал - как кто-то теплый подлез мне под руку и улегся рядом..."
    
    scene bg black with fade
    $ renpy.pause(2, hard=True)
    scene bg int_catacombs_living
    show uv smile close at center with dissolve
    
    "Проснулся я от ощущения какой-то тяжести на груди."
    "\"Завалило!\" - была первая паническая мысль."
    "Но нет, это была всего-лишь Юля."
    "Она лежала, опершись локтями мне на грудь, и пристально изучала меня. Какое-то время мы молча смотрели друг на друга."
    uv "Я вчера двоих ваших видела, старших. У речки. Большой, тяжёлый такой, и та, с которой ты живёшь."
    me "Ага... И что они делали?"
    uv "Спаривались."
    "Я вытаращил глаза."
    me "Чего-о?! Ольга Дмитриевна и Саныч?!"
    dreamgirl "Вот это поворот!"
    uv "Ага. Интересно было, я раньше не видела, как это. Непохоже."
    me "На что непохоже?"
    uv "На других зверей. Не как белки. Или мыши. Их тогда легко ловить."
    menu:
        "Сменить тему":
            pass
        "Узнать поподробней":
            $ alt_day5_uv_hentai = True
        
            me "По-другому - это как?"
            uv "Ну вот так. Сначала просто сидели."
            
            "Она взяла мои руки и положила себе на спину. Опа, а куда это ее платье подевалось?"
            uv "Потом вот так."
            "Она прижалась носом к моему носу. Наверное, это должно означать поцелуй."
            uv "Потом вот."
            "Чуть повернулась боком, и прижала мою ладонь к своей груди."
            dreamgirl "Чувааааак? Кажется, нам дадут!"
            th "Но она же… не человек?"
            dreamgirl "Сиська вполне человеческая. И, кстати, совсем не маленькая. Да и все остальное, кроме хвоста и ушей - тоже."
            th "Да я не об этом! Если б такое устроила обычная девушка - все ясно на сто процентов. А вот что у нее в голове происходит... я ж вам не какой-нибудь контактер-уфолог!"
            dreamgirl "И разделась она просто так, ага. Поверь мне, если ее перестанет устраивать происходящее, тебе об этом сообщат. В виде огромных царапин на всю щёку. Ну или пощёчину влепит, если ей хоть немного понравилось."
            uv "А потом уже вот так!"
            "Она вскочила на четвереньки и повернулась ко мне, при этом хитро поглядывая через плечо, на манер избушки, так сказать. К стене передом, к Семёну задом."
            dreamgirl "Ну, убедился?"
            "Юлин хвост изогнулся эдаким приглашающим знаком вопроса. Не дождавшись от меня какой-нибудь реакции, она потопталась коленями и вопросительно наклонила голову."
            uv "М-рррр?"
            dreamgirl "Перевожу: Ну и долго тупить будем? Барышня готова и ждёт своего кавалера."
            "Нет смысла противиться неизбежному. Не то чтоб происходящее оставило меня равнодушным, совсем наоборот, но... Блин, это же бред какой-то! Или эротический сон."
            dreamgirl "Если сон, то тем более нечего тормозить. Короче, ты меня достал!"
            
            play music music_list["i_dont_blame_you"]
            
            "Меня подняло с кровати каким-то внезапным импульсом - должно быть, это тот самый пресловутый \"Внутренний пендель\"."
            "Только сейчас я обнаружил, что и рубашка давно валяется на полу, и шорты на мне расстегнуты..."
            "А времени она не теряла. Пока я сидел она своим хвостом чуть-ли полностью не раздела меня."
            "Руки сами собой легли на её талию, притянули к себе."
            uv "Мрррррра-а-у-у-у!"
            "Oдобрительно протянула она и соблазнительно прогнулась."
            th "Будь я котом, я бы просто взял её зубами за шкирку и хардкорно отымел..."
            dreamgirl "Как будто что-то плохое. Да и она вряд ли будет против."
            th "Цыц. Я пытаюсь не посрамить гордое звание Гомо Сапиенса в первом контакте с иной расой!"
            "Вместо этого, я наклонился и прикоснулся губами чуть выше копчика. Хвост немедля обвил мне шею, будто какой-то пушистый удав, и затрепетал кончиком у меня на груди."
            "Дальше - цепочка поцелуев вдоль позвоночника, руки, облапившие грудь... Когда я дошёл до места между лопаток..."
            uv "Мррра-а-а-у-у-а-а-у-у!"
            "Она немного преподнялась сзади и поводила своими ягодицами около меня."
            dreamgirl "Это означает: Ну не тяни уже! Ваш К.О. всегда рад помочь."
            "Желание девочки - закон. А уж кошкодевочки... Я в единый миг освободился от всего, что мешало мне ниже пояса, и, прицелившись..."
            dreamgirl "На ладонь ниже хвоста. Не промахнись, Ястребиный Глаз."
            uv "Мааааауууу..."
            "...единым махом скользнул внутрь."
            "Она с вздохом качнулась сначала от меня, потом обратно... И снова... И снова, вовлекая меня в движения."
            "Старая железная конструкция душераздирающе скрипела и качалась. Оставалось надеяться, что проектировщики заложили приличный запас прочности, и эта бандура не обрушится нам на головы. Впрочем, нас это мало беспокоило - мы как раз нашли подходящий ритм, и не собирались останавливаться несмотря ни на что!"
            "Юля с каждым движением старалась выгнуться все сильнее, её кошачьи стоны заглушали скрип, а я... Я так увлекся ролью \"кота\", что стал даже подпевать ей. Кажется, мы движемся к финалу..."
            "Хвост её по-прежнему обвивался вокруг меня, щекоча и вздрагивая. Я прижал его рукой к животу, и тон её \"песен\" внезапно повысился на октаву, вместе с громкостью. Ого! Вот это находка!"
            "Я не преминул воспользоваться новым знанием эрогенных зон кошкодевочек - обхватил ладонью хвост у основания и несильно, но властно потянул к себе. Кошечка прогнулась совершенно невероятным образом, и натурально взвыла, продолжая насаживаться на меня."
            uv "А-а-а-а-х."
            "Это стало первым камешком лавины, и я совершенно потерял самоконтроль. Несколько секунд - или минут? - безумных телодвижений под дикие животные вопли, и мы оба, тяжело дыша, мокрые от пота и прочих жидкостей, повалились обратно на кровать."
            uv "Мррррр... Да, примерно вот так и они тоже."
            "Тяжело дыша сказала она, устраиваясь головой на моём плече."
            me "Они? Кто?"
            "Мозг напрочь отказывался работать."
            uv "Тот большой и вожатая. Только у неё хвоста нет. Жалко ее. С хвостом лучше."
            "Я представил Ольгу Дмитриевну с пушистым кошачьим хвостом, торчащим из-под юбки, и фыркнул. А если ещё уши, да панаму сверху... Не удержавшись, я захихикал совершенно по-дурацки."
            uv "Ты что?"
            "Удивлённо подняла голову Юля."
            me "Представил ее с хвостом и ушами."
            uv "Ааа. Тогда ладно."
            "Она взяла мою ладонь и положила себе на голову. Внегласно намекая - гладь давай, не отвлекайся!"
            "Так мы и лежали, я - почесывая ей между ушами, она - уткнувшись мне в плечо и посапывая."
            dreamgirl "Поздравляю вас, многоуважаемый коллега!"
            "С Шизой говорить желания не было, однако он не оставлял попытки докопаться до меня."
            dreamgirl "Видел бы ты себя со стороны, кошачий угодник."
            menu:
                "Проигнорировать":
                    pass
                "Побеседовать с Шизой":
                    pass
            return
        