# Д6-Обед с Алисой или Славей (свободный выбор)
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines
# Используется флаг alt_uvao_D5_hentai
# используется флаг сопровождения в Д1 Славей от ворот до домика ОД alt_day1_sl_conv
# используется флаг обеда с Леной в 4Д alt_uvao_D4_lunch_un
# используется флаг обеда со Славей в 4Д alt_uvao_D4_lunch_sl
# используется флаг встречи со Славей на пляже в Д5 alt_uvao_D5_evening_sl
# используется флаг встречи с Леной и Алисой на площади вечером Д5 alt_uvao_D5_evening_dv_un
# используется флаг Полной Информированности alt_uvao_D6_CS_vetrov
# используется флаг танцев в д.№3 alt_day3_dancing
# используется флаг защиты Слави от ОД в д.№2 alt_day2_sl_guilty
# используется флаг завтрака со Славей в д.№2 alt_day2_sl_bf
label alt_day6_lunch_dv_sl:
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with fade
    window show
#
# Возможно, здесь нужна минивилка, пришли мы с пляжа или с хозработ - пока что по хозработам ХЗ насчёт подробностей прибытия
#    
    th "Такое ощущение, что пионеров в лагере с каждым днём становится всё больше."
    "Я обвёл взглядом битком набитую столовую."
    "Кажется, столько народу одновременно в местной столовой я до сих пор не видел ни разу."
    th "Размножаются они что ли?"
    dreamgirl "Ага, почкованием, не иначе!"
    if not alt_uvao_D5_hentai:
        dreamgirl "Кстати, и тебе тоже пора осваивать этот метод, судя по твоей вчерашней тормознутости."
        dreamgirl "Это надо же, девочка сама напрашивалась, а он!..."
    "Стараясь не обращать внимания на подколки Шизы, я получил свою порцию еды и снова завертел головой в поисках свободного места."
    "Впрочем, как и за пару минут до этого - безуспешно."
    "Сегодня здесь были буквально все сразу и одновременно."
    if (alt_uvao_true or (not alt_uvao_D5_sh_mines)):
        #Вчера обедали в столовой и Виола жаловалась на пионеров, объевшихся зелёных ягод
        "Даже вчерашние мелкие, наевшиеся зелёных ягод, превозмогли свою смертельно опасную болезнь и явились-таки в столовую."
    th "Да что же это такое! Не стоя же мне есть, не лошадь, всё-таки! Вернее, не конь."
    "Неизвестно, сколько ещё я топтался бы на месте, если бы мне не пришли на помощь."
    show sl smile2 pioneer far at left
    show dv grin pioneer far at right
    with dissolve
    "Сразу две руки поднялись и практически синхронно помахали мне."
    "Лицо Слави выражало искреннее радушие, в жесте Алисы явно угадывалось \"Подь сюды!\"."
    show sl serious pioneer far at left
    show dv sad pioneer far at right
    with dissolve
    "Впрочем, заметив жест друг друга, девочки так же синхронно насупились."
    dreamgirl "Ого, вот это успех! Возможно, всё-таки, для тебя не всё ещё потеряно."
    "Стараясь не рассмеяться, я без особых колебаний поспешил вперёд."
    menu:
        "Сесть с Алисой":
            hide sl with dissolve
            show dv normal pioneer at center with dissolve2
            "Старательно не замечая обиженный взгляд Слави, я подрулил со своим подносом к столику, за которым восседала Алиса."
            "Кажется, сейчас даже возможные подколки Алисы будут лучше, чем становящееся слишком подозрительным внимание активистки. Хорошенького понемногу."
            me "Свободно, подруга?"
            if alt_uvao_D4_lunch_un:
                show dv surprise pioneer
                show un shy pioneer far at fright
                with dissolve
                "Сидевшая неподалёку Лена бросила на меня странный взгляд, но тут же снова уткнулась в тарелку."
                "Особого желания снова играть с ней в гляделки у меня не было, так что я предпочёл её проигнорировать."
                hide un
            show dv surprise pioneer close
            with dissolve
            "Не дожидаясь ответа Алисы, я плюхнулся на свободное место напротив."
            dreamgirl "Что это с тобой? Был такой воспитанный мальчик..."
            th "Как говорится, с волками жить - по-волчьи выть! И вообще, я есть хочу!"
            show dv normal pioneer close with dissolve
            "Впрочем, Алиса, кажется, отнеслась к моей решительности с одобрением."
            show dv smile pioneer close with dspr
            "Откинувшись на спинку стула и ехидно улыбнувшись, она ответила:"
            dv "Приятного аппетита... дружок!"
            "Тут она хихикнула, превратившись на несколько секунд из надменной задиры в обычную рыжеволосую девочку-подростка."
            dreamgirl "Не одна Славя сегодня демонстрирует неожиданные стороны характера.{w} Может, праздник какой, а мы и не знаем?"
            show dv normal pioneer close with dspr
            "Вообще-то, день сегодня и вправду был необычный."
            "Обратив наконец внимание на содержимое тарелки, я обнаружил, что повара расстарались и приготовили на первое солянку."
            "Настоящую ароматную солянку, огненно-красную, с янтарными блёстками жира на поверхности, сквозь которые просвечивали уварившиеся кусочки копчёного мяса."
            th "Надо же, даже каперсы где-то добыли!"
            "Тут наконец до меня дошло:"
            th "Ну да, так последний же день! Прощальный обед и всё такое.{w} То, что половина лагеря будет животами маяться потом - непринципиально."
            "Впрочем, меня эти ньюансы сейчас волновали мало."
            "Бережно размешав сметану и отогнав в сторону подвернувшуюся некстати дольку лимона, я с вожделением зачерпнул первую, самую вкусную ложку..."
            dreamgirl "Эх, Семён, променял ты кошечку на солянку!"
            th "Изыди нечистый, не отравляй радость бытия!"
            "Алиса, до этого молча наблюдавшая за моими манипуляциями, подала наконец голос:"
            show dv grin pioneer close with dissolve
            dv "А ты неплохо устроился!"
            "Не отрываясь от еды, я промычал невнятно:"
            me "Само собой, на том стоим!"
            "Но тут же поинтересовался на всякий случай:"
            me "А что, собственно, ты имеешь в виду?"
            dv "Ну как же! И в медпункт ходишь, как на работу, {i}болтаешь{/i} там с Виолой во время {i}процедур{/i}..."
            "Алиса так похоже изобразила бархатистый, с придыханием, голос Виолы, что мне пришлось прикусить губу, чтобы не рассмеяться."
            dv "...И активисточка наша всё время рядом с тобой вьётся..."
            if alt_uvao_true:
                # пришли на обед с пляжа
                "Обсуждать с Алисой тему внезапно прорезавшейся любезности со стороны Слави мне не очень-то хотелось, и я перебил рыжую, брякнув первое, что пришло в голову:"
                me "Ага, и на пляже бесплатно эротические шоу показывают. Я себя прямо-таки настоящим повелителем гарема чувствую!"
                show dv shy pioneer close with dissolve
                "Наблюдая, как Двачевская заливается краской до самых ушей, я почувствовал себя отомщённым."
                show dv rage pioneer close with dissolve
                "Воровато оглянувшись по сторонам, не подслушивает ли кто, она наклонилась и зашипела на меня:"
                dv "Да что ты мелешь, придурок! Кому ты нужен, чтобы тебе..."
                "Тут она гордо вздёрнула нос и бросила пренебрежительно:"
                show dv shy pioneer close with dissolve
                dv "И вообще, ты сам на меня пялился!"
                "Я изобразил виноватую гримасу и притворно вздохнул:"
                me "Ну да, пялился немножко. Житие мое..."
                me "А с другой стороны, ну кто бы на моём месте устоял перед такой красотой?{w} Ручаюсь, что никто!"
                dreamgirl "Тоже мне, хентай-мастер нашёлся! С таким изяществом только носорогов очаровывать."
                show dv angry pioneer close with dissolve
                "Алиса бросила на меня сердитый взгляд и буркнула:"
                dv "Поговори мне тут ещё!"
            else:
                #пришли на обед с хозработ
                "Обсуждать с Алисой тему внезапно прорезавшейся любезности со стороны Слави мне не очень-то хотелось, и я нейтрально пожал плечами:"
                me "Что же делать, я натура утончённая, меня тянет к прекрасному."
                show dv sad pioneer close with dissolve
                dreamgirl "Ты что мелешь? Тебе давно тарелку на голову не надевали?"
                "Прежде чем Алиса успела всерьёз обидеться, я поторопился выправить ситуацию, наклонившись к ней и доверительно сообщив:"
                me "Раз уж самая красивая девушка лагеря на меня не смотрит, даже шансов никаких, то приходится довольствоваться вторым классом!"
                "Я развёл руками и театрально вздохнул."
                dreamgirl "Тоже мне, хентай-мастер нашёлся! С таким изяществом только носорогов очаровывать."
            show dv grin pioneer close with dissolve2
            "Впрочем, судя по вновь проступившему на щеках Алисы румянцу и скользнувшей на её губы самодовольной ухмылке, мой неуклюжий \"комплимент\" попал в цель."
            "Мне даже немного жаль стало девушку - похоже, до меня на дистанцию прицельного комплиментометания ни один парень к ней не приближался."
            dreamgirl "Я так думаю, что если какие-то камикадзе и пытались, то она отстреливала их ещё на дальних рубежах."
            if not alt_day1_sl_conv:
                "Вспомнив непрошенный душ из пожарного ведра сразу по прибытии, я поёжился."
                th "Действительно, после такого начала мало кто захочет {i}усугублять{/i} знакомство."
            show dv normal pioneer close with dissolve
            if alt_uvao_D4_lunch_un:
                # Если есть флаг обеда с Леной в 4Д alt_uvao_D4_lunch_un, Алиса упоминает о изменении поведения Лены.
                "Приканчивая остатки солянки, я заметил краем глаза, что Лена встала из-за стола и потащила свой поднос в сторону посудомойки."
                show dv sad pioneer close with dissolve
                "Погрустневшая вдруг Алиса проводила её задумчивым взглядом. Потом, отставив в сторону суповую тарелку, так же задумчиво уставилась на плов."
                "Не то, чтобы мне жизнь была не мила без болтовни Алисы, но её дурное настроение не обещало ничего хорошего всем окружающим, включая меня, так что я попытался немного разрядить обстановку."
                me "Похоже, у Лены аппетит не то очень хороший, не то очень плохой, раз она так быстро закончила обед, да?"
                dv "Лена сильно изменилась за последнее время."
                "Сообщила мне Алиса, подняв на меня ставший непривычно серьёзным взгляд."
                dv "С тех пор, как ты приехал."
                dv "Я её хорошо знаю...{w=0.8} Ну, вернее, как хорошо...{w=1.5} Лучше других здесь, во всяком случае. Мы живём недалеко и не первый год уже дружим."
                dv "Она всегда была... {w=0.8}немного замкнутая. Но сейчас совсем в себя ушла, молчит всё время."
                show dv angry pioneer close with dissolve
                "Алиса с досадой качнула головой и угрожающе зыркнула на меня исподлобья."
                th "Эй, а я-то здесь при чём?"
                "Замкнутой мне Лена показалась с самого первого дня, тут и говорить не о чем. Но при чём здесь мой приезд?"
                show dv sad pioneer close with dissolve
                "Молча покачав головой, Алиса принялась вяло ковырять вилкой плов."
            else:
                "Отставив в сторону суповую тарелку, Алиса задумчиво принялась ковырять вилкой плов."
            if alt_uvao_D5_evening_dv_un:
                # Если есть флаг вечера 5д alt_uvao_D5_evening_dv_un - о том, что, похоже, Лена втрескалась в Cемёна.
                dv "Кстати, о любовании красотой... Возможно, тебе стоило бы побольше пялиться немного в другую сторону."
                "Я недоумённо посмотрел на Алису."
                show dv angry pioneer close with dissolve
                dv "Ну чего уставился? Можно подумать, кроме твоей активисточки здесь других девчонок нет!"
                "Алиса бросила на Славю злобный взгляд и, наклонившись над столом, продолжила вполголоса:"
                show dv sad pioneer close with dissolve
                dv "В общем, я пристала к ней с расспросами, и она не выдержала, всё мне рассказала..."
                show dv shy pioneer close with dissolve
                "Тут Алиса запнулась, явно смутившись. Отведя взгляд в сторону, она закончила невнятной скороговоркой:"
                dv "Короче, она в тебя втюрилась, вот!"
                "Выпрямившись, она скрестила руки на груди и бросила на меня сердитый взгляд, словно я только что заставил её признаться в чём-то постыдном."
                "Поняв, что продолжения не будет, я спросил вкрадчивым голосом:"
                me "Слушай, Алиса, а ты о ком, вообще-то, говоришь?"
                show dv angry pioneer close with dissolve
                dv "Дурак!"
                "Окрысилась она на меня, и я немедленно вспомнил это же самое слово, произнесённое этой же самой девочкой не далее, как вчера вечером!"
                th "Подождите, неужели всё-таки..."
                "Алиса не замедлила развеять остатки моих сомнений, вновь перейдя на угрожающее шипение:"
                dv "Да о Ленке я говорю, о ком же ещё! Нельзя же быть таким тормозом!"
                "Проглотив оскорбление, я ошарашенно уставился на Алису."
                me "А...а... а ты уверена?"
                show dv surprise pioneer close with dissolve
                dreamgirl "Да, ты действительно туповат. Это факт. Не повезло мне с носителем."
                "Похоже было, что Алиса тоже окончательно уверилась в невысоком уровне моих умственных способностей, потому что в ответ она лишь покачала головой и вздохнула:"
                show dv sad pioneer close with dissolve
                dv "Верно говорят - \"любовь зла, полюбишь и козла\". Бедная Лена..."
                "После этого Двачевская скорчила зверскую рожу и процедила, угрожающе сжимая кулаки:"
                show dv angry pioneer close with dissolve
                dv "Смотри мне, не вздумай ляпнуть кому-нибудь, что это я тебе рассказала!"
                "Я поспешно замахал руками, мол, буду нем как рыба, но она всё-таки закончила, перейдя на зловещий шёпот:"
                dv "Короче говоря, одно неосторожное слово, даже взгляд, и ты - покойник."
            "Остаток обеда прошёл в молчании."
            show dv normal pioneer close with dissolve
            if alt_uvao_D5_evening_dv_un:
                "Алиса явно не была склонна продолжать разговор, а я тоже решил, что уже и так узнал больше, чем рассчитывал."
                "К тому же мне совсем не хотелось нарываться. Быть поколоченным девчонкой..."
                "Я нисколько не сомневался ни в том, что угрозы Алисы не были шуткой, ни в том, что за ней не заржавеет их выполнить."
            if (alt_uvao_D4_lunch_un or alt_uvao_D5_evening_dv_un):
                # Наслушались Алису и задумываемся о Лене
                "Машинально работая челюстями, я обдумывал услышанное от Алисы."
                window hide
                $ set_mode_nvl()
                window show
                # TODO при отладке повставлять очистку экрана nvl clear где потребуется
                if alt_uvao_D5_evening_dv_un:
                    # Знаем про влюблённость Лены от Алисы
                    th "Неужели, Лена и вправду в меня... гм... {i}втюрилась{/i}? Час от часу не легче."
                    "Приходилось взглянуть правде в глаза - большая часть заморочек Лены этим вполне объяснялась.{w} Например, то, что она напросилась идти искать Шурика и жутко смутилась, когда Ольга об этом проболталась..."
                else:
                    # Алиса не рассказывала про влюблённость Лены (но всё равно обедали с Леной в Д4)
                    "По всему выходило, что не мне одному поведение Лены показалось странным."
                    "Да что там \"показалось\" - оно и было странным! Эти её неловкие попытки заговорить со мной, то, что она напросилась идти искать Шурика и её смущение, когда Ольга об этом проболталась..."
                    th "Неужели Лена и вправду в меня влюбилась? Час от часу не легче."
                th "Но странно, очень странно!{w} Это только в романах так бывает, что встретились глазами, и р-р-раз, готово! Любовь до гробовой доски!"
                th "Внешность у меня заурядная, интеллектом-шутками блеснуть возможности никакой не было. Да если бы даже и была..."
                th "Мы вообще, если на то пошло, почти и не общались, а Лена чуть ли не с первого дня демонстрировала все признаки..."
                th "Нет, определённо что-то здесь не так."
                "Меня не покидало смутное ощущение, что я что-то упускаю."
                if (alt_uvao_D4_lunch_un and alt_uvao_D5_evening_dv_un and alt_uvao_D6_CS_vetrov):
                    # собрали все три флага - Семён подозревает о кошочкином участии.
                    # Замечаем Мику. Они же соседки, вроде бы! Может, она тоже что-нибудь заметила? Хорошо бы поговорить с ней.
                    nvl clear
                    dreamgirl "Мне тоже кажется, что ты кое-что упускаешь. Так и быть, дам тебе подсказку."
                    dreamgirl "Пораскинь мозгами - кто ещё в лагере вёл себя странно за то время, что ты здесь?"
                    th "Ты опять издеваешься? Да здесь половина лагеря себя странно ведёт, начиная со всё той же Лены и заканчивая Шуриком!"
                    th "Минуточку..."
                    dreamgirl "Бинго."
                    "Удовлетворённо констатировал голос в моей голове."
                    dreamgirl "Конечно, это можеть быть простым совпадением..."
                    th "...но как минимум у двух человек с интервалом всего в несколько дней съезжает набекрень крыша..."
                    dreamgirl "...причём про одного их них мы знаем наверняка, что ему в этом здорово помогла Юля!"
                    "Я откинулся на спинку стула."
                    nvl clear
                    th "Действительно, что если Лена столкнулась с хвостатой, той что-то не понравилось, ну и... Шурик после {i}обработки{/i} начал голоса слышать, а Лена по-своему могла отреагировать."
                    th "Вообще-то, можно попробовать порасспросить кого-нибудь, кто её хорошо знает. Вот только вопрос - кого? Она же стесняша нелюдимая."
                    dreamgirl "Ты мог и не заметить, но прямо перед тобой её подруга сидит - её и расспрашивай."
                    th "Нет уж, дудки! Я жить хочу!"
                    dreamgirl "Ну так с соседкой Лены поговори, с японкой этой! Подруги они или нет, но Лену она как минимум дважды в день видит. Вполне могли перед сном о своём, девчоночьем, поболтать-посплетничать."
                else:
                    "В законченную мысль это ощущение, впрочем, так и не оформилось, а обычно болтливое не в меру альтер эго на этот раз помалкивало."
                show dv angry pioneer close with dspr
                with vpunch #проверить
                window hide
                $ set_mode_adv()
                window show
                dv "Эй, на барж{b}е{/b}?!"
                "Вздрогнув от звонкого щелчка пальцами под самым носом, я понял, что уже пару минут сижу с недонесённой до рта вилкой и тупо пялюсь куда-то Алисе за спину."
                "Хмыкнув, рыжая заботливо предложила:"
                show dv grin pioneer close with dissolve
                dv "Слушай, может тебе в лоб двинуть? В лечебно-профилактических целях?"
                if alt_uvao_true:
                    # пришли на обед с пляжа
                    "Рука сама собой потянулась ощупать ушибленную при посещении пляжа часть тела. Увидев это, Алиса язвительно фыркнула, а я, смутившись, буркнул что-то невнятное и уставился в свою тарелку."
                else:
                    "Смутившись, я буркнул что-то невнятное и уставился в свою тарелку."
                show dv normal pioneer close with dissolve
            else:
                # О Лене не думаем.
                # Текст не нужен.
                pass
            "Не сговариваясь, мы с Алисой по-быстрому прикончили свои порции, залпом выпили неизбежный компот и поспешили было освободить помещение столовой, но были остановлены властным жестом Ольги."
            # ЛБ: необходимо наверняка сообщить ГГ про предстоящий концерт. Как минимум, потребуется при поисках Мику.
            show dv normal pioneer at cright
            show mt normal pioneer at left
            with dissolve
            mt "Минуточку внимания, пожалуйста!"
            $ renpy.music.set_volume(0.3, delay=2, channel='ambience')
            "Сильный голос вожатой легко перекрыл обычный шум столовой, заставив все головы повернуться к ней."
            show mt smile pioneer at left with dspr
            mt "Ребята, напоминаю вам ещё раз, что полдник сегодня будет на сорок минут раньше, а сразу после него начнётся итоговый концерт! Обещаю, будет интересно, так что не опаздывайте!"
            $ renpy.music.set_volume(1.0, delay=3, channel='ambience')
            mt "Явка на концерт, кстати, обязательна для всех."
            "Сообщила она уже нормальным голосом, обращаясь непосредственно ко мне.{w} Я послушно кивнул и был наконец милостиво отпущен следом за Алисой."
            stop ambience fadeout 2
            hide mt with dissolve
            hide dv with dissolve
            window hide
            scene bg ext_dining_hall_near_day with dissolve
            play ambience ambience_camp_center_day fadein 2
            show dv normal pioneer far at left with dissolve
            window show
            if (alt_uvao_D4_lunch_un and alt_uvao_D5_evening_dv_un and alt_uvao_D6_CS_vetrov):
                #ЛБ: Если дальше свернём на Мику, то зажигалочка эта пригодится утром Д7. Если не свернём... там видно будет.
                "Выйдя из столовой, Алиса бросила на меня косой взгляд и устремилась было к ступенькам, как вдруг что-то звонко цокнуло по бетону крыльца, блеснув на солнце."
                "Я нагнулся было за оброненным девушкой предметом, но та оказалась проворнее. Металлический брусочек бензиновой зажигалки промелькнул перед моим лицом, чтобы тут же исчезнуть в кармане."
                show dv angry pioneer with dissolve
                "Алиса сердито зыркнула на меня исподлобья, но промолчала. Через секунду она уже целеустремлённо неслась куда-то в сторону площади."
                th "Ишь, какая колбаса деловая. Зажигалка у неё, как у {i}взрослой{/i}..."
            else:
                "Выйдя на улицу, Алиса бросила на меня косой взгляд и устремилась куда-то в сторону площади."
            hide dv with moveoutleft
            if (alt_uvao_D4_lunch_un and alt_uvao_D5_evening_dv_un):
                # Задумываемся, куда бежать дальше, чтобы выяснить всё-всё про Лену
                "Я притормозил на крыльце, прикидывая, что делать дальше."
                menu:
                    "Поговорить с Мику" if alt_uvao_D6_CS_vetrov:
                        jump alt_day6_uvao_left_ask_MI_about_UN
                    "Искать Юлю":
                        jump alt_day6_uvao_left_ask_UV_about_UN
                    "Не надо суеты!":
                        # Валим из столовой без конкретных намерений - "там видно будет", нас ловит Славя
                        "Прислонившись к перилам, я сыто вздохнул."
                        th "Собственно говоря, а чего это я задёргался?"
                        th "Ну влюбилась в меня Лена, дальше-то что?"
                        th "Всё равно сегодня последний день. Выяснять отношения теперь уже в любом случае поздно - одно только расстройство получится."
                        th "Тем более, что Лена действительно... того... необщительная. Хватит с меня этих игр в гляделки-молчанки."
                        th "Через сутки мы так или иначе, но разбежимся в разные стороны, лучше уж просто подождать."
                        "Что-то похожее на совесть попыталось было поднять голову, но я поспешил придавить этого гнусного червячка:"
                        th "А ну цыц! Не умею я эти разговоры о чувствах вести, а уж тем более - признаваться в отсутствии взаимности."
                        dreamgirl "Не кричи. Я вообще молчу, между прочим."
                        "Голос Шизы показался мне укоризненным, и я немедленно огрызнулся:"
                        th "А я, между прочим, и не к тебе обращаюсь!"
                        "Подспудно я ожидал в ответ какой-нибудь шуточки про растроение личности, но своенравное подсознание промолчало, что меня вполне устраивало."
                        if alt_uvao_D6_CS_vetrov:
                            pass
                            th "Если подумать хорошенько, то даже если это и впрямь Юлиных рук дело, то чем я-то смогу Лене помочь?{w} Шурика, вон, отпустило - значит и её отпустит. Само как-нибудь рассосётся."
                        "Наверное, я бы ещё какое-то время мялся в нерешительности, но тут меня как громом поразила простая мысль:"
                        th "Минуточку! А что если эта рыжая мне всё наврала про Лену? С неё ведь станется!"
                        "Я представил себе, как подъезжаю к Лене с объяснениями, а та в ответ смотрит на меня, как на последнего идиота, и меня бросило в жар."
                        th "Нафиг!"
                        "Тряхнув головой, я постарался выбросить все эти дурные идеи из головы."
            else:
                pass
            # Разговор со Славей у столовой
            #===== TODOtext
            # "собрался туда-не-знаю-куда, как меня окликнул знакомый голос"
        "Сесть со Славей":
            hide dv
            show sl smile pioneer at center
            with dissolve
            jump alt_day6_lunch_dv_sl_1
    #===== TODOtext
    # Посчитать, что беседа будет о делах амурных (Можно помечтать на веранде столовой)
    # Топаем в домик
    window hide
    scene bg black with fade
    stop ambience
    stop music
    stop sound
    stop sound_loop
    jump scenario_uvao_debug
                
