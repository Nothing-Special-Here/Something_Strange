#
# Д5-вечер - наблюдаем на площади ДваЧе и Унылку
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines (Видели Шурика в шахтах/не обедали/спалились на стоянке)
# используется флаг обеда в Д4 с Леной alt_uvao_D4_lunch_un
# устанавливает флаг встречи с ДваЧе и Унылкой alt_uvao_D5_evening_dv_un
#
label alt_day5_uvao_evening_dv_un:
    scene bg ext_dining_hall_away_sunset with fade
    th "Не думаю, что на площади за это время появилось что-то интересное, но почему бы и нет? Убить время можно и там."
    th "Посижу после еды на скамеечке, подумаю о политике. Вряд ли кроме меня там кто-то будет."
    dreamgirl "А ты не боишься, что если ты начнёшь считать ворон в самом центре лагеря, то тебя мигом привлекут к каким-нибудь общественным работам?"
    if alt_uvao_D5_sh_mines:
        th "Пусть только попробуют! К тому же, мне ведь ясно пообещали \"более комфортные\" условия пребывания - вот и проверим, чего стоят эти слова."
    else:
        th "Пусть только попробуют! На сегодня я свой общественный долг уже исполнил с лихвой - до сих пор не могу рук поднять."
        if alt_uvao_true:
            th "И вообще, я при исполнении! Мысленный эксперимент буду ставить!"
    window hide
    scene bg ext_square_sunset with dissolve
    $ renpy.pause(1)
    window show
    "До площади оставалась пара шагов, когда я обнаружил, что ближайшая лавочка уже занята - на ней сидели голова к голове две девочки, занятые негромким разговором."
    stop music fadeout 3
    "В лучах закатного солнца рыжие волосы одной из них пылали красной медью, а смешные хвостики на голове второй казались сейчас сиреневыми."
    show un normal pioneer far at cright
    show dv normal pioneer far at fright
    with dissolve
    th "Вот уж не ожидал увидеть Алису и Лену вместе! Что у них может быть общего?"
    dreamgirl "А вот интересно, Лена волосы красит в синий цвет, или они у неё такие от природы?"
    th "Синих волос не бывает…"
    dreamgirl "Это в {i}том{/i} мире не бывает синих волос, точно так же, как и девочек с кошачьими ушами и хвостом, кстати говоря. Только вот ты-то не там, а {i}здесь{/i}."
    "Занятые разговором девочки пока что не замечали моего появления, но продолжаться бесконечно это не могло."
    th "В \"том\" я мире, или не в \"том\", но у меня такое ощущение, что лучше бы мне уйти подобру-поздорову, пока они меня не увидели. Решат ещё, что подслушиваю."
    if alt_uvao_true:
        th "Тем более, Лена достаточно странно себя вела сегодня. Не вышло бы сейчас какого-нибудь продолжения."
    elif alt_uvao_D4_lunch_un:
        th "Тем более, Лена вчера достаточно странно себя вела. Не вышло бы сейчас какого-нибудь продолжения."
    "Я сделал было осторожный шаг назад, но тут Лена подняла голову и заметила меня."
    show un shocked pioneer far with dissolve
    "Пару секунд она смотрела на меня широко раскрытыми глазами, словно кролик на удава.{w} Потом, словно её за ниточки дёрнули, вскочила на ноги."
    un "Я...Я...ЯДОЛЖНАИДТИУМЕНЯДЕЛА."
    "Всхлипнув что-то нечленораздельное, она опрометью бросилась бежать."
    hide un with easeoutright
    play music music_list["pile"] fadein 3
    show dv rage pioneer far with dissolve
    "Алиса резко поднялась на ноги. Я не успел и глазом моргнуть, как она уже подступала ко мне, сжав кулаки."
    show dv rage pioneer at center with dissolve
    dv "Ты… Ты… Ты подслушивал, гад!"
    "Ошеломлённый, я невольно попятился назад от разгневанной рыжей."
    me "Алиса, ты что? Ничего я не подслушивал, я вообще только что подошёл!"
    show dv rage pioneer close at center with dissolve
    "Пятясь, я выставил перед собой руки, не то в примиряющем жесте, не то готовясь прикрывать лицо от ударов продолжающей наступать на меня Двачевской."
    me "Я вас не сразу заметил, а как увидел - сразу хотел уйти, чтобы не мешать! Честное пионерское…"
    show dv angry pioneer close at center with dissolve
    "Алиса остановилась, по-прежнему глядя на меня исподлобья и тяжело дыша. Я поспешно добавил:"
    me "И вообще, даром не нужны мне ваши секреты, охота была подслушивать!"
    "Реакция была совершенно неожиданной."
    show dv sad pioneer close at center with dissolve
    dv "Дурак!"
    "Крикнула внезапно тонким голосом Алиса."
    stop music fadeout 3
    hide dv with easeoutright
    "Не говоря больше ни слова, она повернулась и зашагала прочь, печатая каждый шаг так, словно мечтала пригвоздить меня подошвой к бетонным плитам площади."
    me "…"
    "Открыв рот, я какое-то время смотрел ей вслед."
    th "Да что они здесь, с ума все посходили, что ли? Не пионерский лагерь, а какой-то дурдом на выезде! Ничего не понимаю."
    dreamgirl "Только меня ни о чём не спрашивай. Я беру отгул за свой счёт, извини."
    "Я перевёл дыхание и вытер ладонью вспотевший лоб. Кажется, лучшее, что мне оставалось сейчас сделать - это отправляться немедленно к своему домику и постараться больше не влипнуть сегодня ни в какую историю."
    $ alt_uvao_D5_evening_dv_un = True
    jump alt_day5_uvao_evening_headlong