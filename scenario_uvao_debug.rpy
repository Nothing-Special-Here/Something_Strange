init python:
    def make_names_known_7dl():
        make_names_known()
        global store
        set_name('ba',u"Саныч")
        set_name('ase',u"Алиса")
        set_name('we',u"Толпа")
        set_name('ml',u"Мальчик")
        set_name('ml2',u"Мальчик")
        set_name('voice1',u"Продавщица")
        set_name('kids',u"Дети")
        set_name('dy',u"Динамики")
        set_name('icq',u"Собеседник")
init:
    $ mods["scenario_uvao_debug"] = u"ЮВАО рут - отладка"
    $ config.developer = True
    $ herc = False
    $ loki = False

    $ th_prefix = "«"
    $ th_suffix = "»"
    
    $ mod_tags["scenario_uvao_debug"] = ["length:days","gameplay:vn","protagonist:male","special:TODO","character:Виола","character:Алиса","character:Электроник","character:Семён","character:Мику","character:Ольга Дмитриевна","character:Женя","character:Пионер","character:Шурик","character:Славя","character:Лена","character:Ульяна","character:Юля"]
    $ routetag = "uvao"
label scenario_uvao_debug:
    $ make_names_known_7dl()
    $ set_mode_adv()
#
# Флаг посещения медпункта
    $ alt_uvao_D4_viola_morning = False
# Флаг попадания с обеда на концерт
    $ alt_uvao_D4_concert = False
# Флаг обеда с Леной 
    $ alt_uvao_D4_lunch_un = False
# Флаг обеда со Славей
    $ alt_uvao_D4_lunch_sl = False
# Флаг хентая в бункере
    $ alt_uvao_D5_hentai = False
# Флаг "нахождения" Шурика в шахтах
    $ alt_uvao_D5_sh_mines = False
# Флаг выхода на тру-энд alt_uvao_true
    $ alt_uvao_true = False
# Флаг встречи со Славей вечером Д5 alt_uvao_D5_evening_sl
    $ alt_uvao_D5_evening_sl = False
# Флаг встречи с ДваЧе и Унылкой alt_uvao_D5_evening_dv_un
    $ alt_uvao_D5_evening_dv_un = False
# Флаг полной информированности от Виолы
    $ alt_uvao_D6_CS_vetrov = False
#
# приходит из Д1
    $ keys_keep = True
    $ keys_take = 1
    $ dv_help = 1
# из Д3
    $ alt_day3_duty = False
#
    jump scenario_uvao_root_D4_debug
   
label scenario_uvao_root_D4_debug:

    menu:
        "Отладка: Встреча Юли в д3":
            call alt_day3_meet_uvao
        "Прохождение Д4 по порядку":
            jump alt_day4_start_uvao
        "Прохождение Д5 по порядку":
            jump alt_day5_uvao_start_debug
        "Прохождение Д6 по порядку":
            jump alt_day6_uvao_start_debug
        "Отладка Д4":
            menu:
                "Уборка гирлянд":
                    jump alt_day4_uvao_garlands_removal_debug
                "Посещение библиотеки":
                    jump alt_day4_uvao_library
                "Сразу Д4-Обед":
                    jump alt_day4_uvao_lunch
                "Сразу Д4-встреча с Юлей после обеда без концерта":
                    $ alt_uvao_D4_concert = False
                    jump alt_day4_uvao_meet_Yulia_after_lunch
                "Сразу Д4-встреча с Юлей после концерта (обедали со Славей)":
                    $ alt_uvao_D4_concert = True
                    $ alt_uvao_D4_lunch_un = False
                    $ alt_uvao_D4_lunch_sl = True
                    jump alt_day4_uvao_meet_Yulia_after_lunch
                "Сразу Д4-встреча с Юлей после концерта (обедали с Леной)":
                    $ alt_uvao_D4_concert = True
                    $ alt_uvao_D4_lunch_un = True
                    $ alt_uvao_D4_lunch_sl = False
                    jump alt_day4_uvao_meet_Yulia_after_lunch
                "Сразу Д4-ужин с Виолой (на выбор)":
                    $ alt_uvao_D4_viola_morning = True
                    jump alt_day4_uvao_supper
                "Сразу Д4-ужин без Виолы":
                    $ alt_uvao_D4_viola_morning = False
                    jump alt_day4_uvao_supper
                "Сразу Д4-встреча с Юлей после ужина":
                    jump alt_day4_uvao_meet_Yulia_at_evening
                "Сразу Д4-после ужина с Виолой":
                    $ alt_uvao_D4_supper_cs = True
                    jump alt_day4_uvao_evening_business
                "Сразу Д4-после ужина без Виолы":
                    $ alt_uvao_D4_supper_cs = False
                    jump alt_day4_uvao_evening_business
                "Назад":
                    jump scenario_uvao_root_D4_debug
        "Отладка Д5":
            menu:
                "Подъём без доклада Виоле в Д4":
                    $ alt_uvao_true = False
                    jump alt_day5_uvao_getting_up
                "Подъём с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_getting_up
                "Спуск в бункер с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_tunnel                
                "Спуск в бункер без доклада Виоле в Д4":
                    jump alt_day5_uvao_tunnel
                "В бункере с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_bunker                
                "В бункере без доклада Виоле в Д4":
                    jump alt_day5_uvao_bunker
                "Поход наверх. Тру рут":
                    jump alt_day5_uvao_true_back
                "Охота на Шурика в шахтах":
                    jump alt_day5_uvao_mines_sh
                "Охота на Шурика в шахтах - сцена пленения":
                    jump alt_day5_uvao_mines_sh_capture_debug
                "Поход назад через стоянку.":
                    jump alt_day5_parking_back_debug
                "Обед без доклада Виоле в Д4":
                    $ alt_uvao_true = False
                    jump alt_day5_uvao_lunch
                "Обед с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_lunch
                "Совместная охота на дикого Шурика not-uvao_true":
                    $ alt_uvao_true = False
                    jump alt_day5_capture_sh_together_debug
                "Совместная охота на дикого Шурика uvao_true":
                    $ alt_uvao_true = True
                    jump alt_day5_capture_sh_together_debug
                "Вечер not-uvao_true":
                    $ alt_uvao_true = False
                    jump alt_day5_uvao_evening_debug
                "Вечер uvao_true":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_evening_debug
                "Славя на пляже":
                    jump alt_day5_uvao_ev_beach_event
                "Назад":
                    jump scenario_uvao_root_D4_debug
        "Отладка Д6":
            menu:
                "Утро":
                    menu:
                        "Тру Ветка":
                            $ alt_uvao_true = True
                        "Палевная Ветка":
                            $ alt_uvao_D5_sh_mines = True
                        "Беспалевная Ветка":
                            pass
                        #Тут должны быть ещё пару условий про хентай и прочее, но это потом.
                    jump alt_day6_uvao_getting_up
                "Хозработы":
                    menu:
                        "Палевная ветка(Со Славей)":
                            jump alt_day6_uvao_duty_sl
                        "Беспалевная ветка":
                            jump alt_day6_uvao_duty
                "Концерт со Славей":
                    jump alt_day6_uvao_concert_with_sl
                "Тру: Утро с Виолой":
                    jump alt_day6_true_CS_talk_debug
                "Тру: Завтрак со Славей":
                    menu:
                        "Был пляж в Д5":
                            $ alt_uvao_D5_evening_sl = True
                            jump alt_day6_true_sl_morning
                        "Не было пляжа в Д5":
                            $ alt_uvao_D5_evening_sl = False
                            jump alt_day6_true_sl_morning
                "Тру: Пляж":
                    jump alt_day6_true_beach_debug
                "Левая: Обед":
                    jump alt_day6_lunch_dv_sl_debug
                "Левая: (после Мику) Начало концерта и посылаем Алису за Леной":
                    jump alt_day6_uvao_left_concert_time_debug
                "Левая: Разборки в медпункте (привели ОД, прибегает Лена)":
                    jump alt_day6_uvao_left_aidpost_debug
                "Левая: Разборки в медпункте (принесли ужин, является Юля)":
                    jump alt_day6_uvao_left_aidpost_battle
                "Изолятор (С домика ОД)":
                    menu:
                        "Хентай был":
                            $ alt_uvao_D5_hentai = True
                        "Хентая не было":
                            $ alt_uvao_D5_hentai = False
                    jump alt_day6_uvao_isolator_house
        "Картинки при смене глав":
        # Крашит игру, грит NameError: name 'alt_chapter_uv' is not defined
            label scenario_uvao_chapters:
                menu:
                    "До первой встречи":
                        $ routetag = "uv_unknown"
                        $ alt_chapter_uv(0, "До первой встречи")
                        jump scenario_uvao_chapters
                    "После знакомства":
                        $ routetag = "uv"
                        $ alt_chapter_uv(0, "После знакомства")
                        jump scenario_uvao_chapters
                    "Выход на бэд":
                        $ routetag = "uv_bad"
                        $ alt_chapter_uv(0, "Выход на бэд")
                        jump scenario_uvao_chapters                    
                    "Выход на фальш":
                        $ routetag = "uv_false"
                        $ alt_chapter_uv(0, "Выход на фальш")
                        jump scenario_uvao_chapters                    
                    "Выход на тру":
                        $ routetag = "uv_true"
                        $ alt_chapter_uv(0, "Выход на тру")
                        jump scenario_uvao_chapters    
                    "Для сравнения - Лена-бэд":
                        $ routetag = "un7dlbad"
                        $ alt_chapter(0, "Леночка плачет")
                        jump scenario_uvao_chapters    
                    "Назад":
                        jump scenario_uvao_root_D4_debug
        "Отладка спрайтов":
            jump scenario_uvao_sprites
        "Отладка фонов":
            jump scenario_uvao_bg

    $ renpy.pause (1)
    jump scenario_uvao_root_D4_debug

label alt_day5_uvao_start_debug:
    menu:
        "Ходили к Виоле утром Д4":
            $ alt_uvao_D4_viola_morning = True
        "Бесславно обруганы ОД утром Д4":
            $ alt_uvao_D4_viola_morning = False
    menu:
        "Обедали в Д4 с Леной":
            $ alt_uvao_D4_lunch_un = True
            $ alt_uvao_D4_concert = True
        "Обедали в Д4 со Славей":
            $ alt_uvao_D4_lunch_sl = True
            $ alt_uvao_D4_concert = True
        "Обедали в Д4 в одиночестве":
            $ alt_uvao_D4_concert = False
            $ alt_uvao_D4_lunch_un = False
            $ alt_uvao_D4_lunch_sl = False
    if alt_uvao_D4_viola_morning:
        menu:
            "Ужинали с Виолой в Д4 (True)":
                $ alt_uvao_true = True
            "Не ужинали с Виолой в Д4 (non-True)":
                $ alt_uvao_true = False
    else:
        $ alt_uvao_true = False
    jump alt_day5_uvao_getting_up

label alt_day6_uvao_start_debug:
    # Глобальный выбор
    menu:
        "Тру-ветка":
            $ alt_uvao_true = True
        "Палевная ветка":
            $ alt_uvao_D5_sh_mines = True
        "Беспалевная ветка":
            pass
    # Всякие флаги предыдущего прохождения
    menu:
        "Обед Д4 - с Леной":
            $ alt_uvao_D4_lunch_un = True
        "Обед Д4 - со Славей":
            $ alt_uvao_D4_lunch_sl = True
        "Обед Д4 - в одиночестве":
            pass
    if not alt_uvao_true:
        menu:
            "Д5 - хентай был":
                $ alt_uvao_D5_hentai = True
            "Д5 - хентая не было":
                pass
    menu:
        "Вечер Д5 - встретили Славю на пляже":
            $ alt_uvao_D5_evening_sl = True
        "Вечер Д5 - встретили Лену и Алису на площади":
            $ alt_uvao_D5_evening_dv_un = True
        "Вечер Д5 - сразу спать":
            pass
            
    jump alt_day6_uvao_getting_up
    
label alt_day5_capture_sh_together_debug:
    menu:
        "Обедали в Д4 с Леной":
            $ alt_uvao_D4_lunch_un = True
            jump alt_day5_capture_sh_together
        "Не обедали в Д4 с Леной":
            $ alt_uvao_D4_lunch_un = False
            jump alt_day5_capture_sh_together
    jump scenario_uvao_root_D4_debug
#
label alt_day5_uvao_evening_debug:
    menu:
        "В Д4 обедали в одиночестве":
            $ alt_uvao_D4_concert = False
        "В Д4 обедали с девочкой":
            $ alt_uvao_D4_concert = True
    if alt_uvao_true:
        $ alt_uvao_D5_sh_mines = False
        $ alt_uvao_D5_hentai = False
    else:
        menu:
            "Хентай был":
                $ alt_uvao_D5_hentai = True
            "Хентая не было":
                $ alt_uvao_D5_hentai = False
        menu:
            "Гоняли Шурика по шахтам":
                $ alt_uvao_D5_sh_mines = True
            "Охотились на Шурика с отрядом":
                $ alt_uvao_D5_sh_mines = False
    jump alt_day5_uvao_evening
#
label alt_day5_parking_back_debug:
    menu:
        "Ходили к Виоле утром Д4":
            $ alt_uvao_D4_viola_morning = True
        "Бесславно обруганы ОД утром Д4":
            $ alt_uvao_D4_viola_morning = False
    menu:
        "Хентай был":
            $ alt_uvao_D5_hentai = True
        "Хентая не было":
            $ alt_uvao_D5_hentai = False
    jump alt_day5_parking_back
#
label alt_day5_uvao_spoiled_supper_debug:
    menu:
        "Ходили к Виоле утром Д4":
            $ alt_uvao_D4_viola_morning = True
        "Бесславно обруганы ОД утром Д4":
            $ alt_uvao_D4_viola_morning = False
    menu:
        "Хентай был":
            $ alt_uvao_D5_hentai = True
        "Хентая не было":
            $ alt_uvao_D5_hentai = False
    jump alt_day5_uvao_spoiled_supper
#
label alt_day6_true_CS_talk_debug:
    menu:
        "В Д5 вечером видел Славю на пляже":
            $ alt_uvao_D5_evening_sl = True
        "В Д5 вечером шлялся где-то ещё":
            $ alt_uvao_D5_evening_sl = False
    menu:
        "В Д2 поддались обаянию Ули и совершили Великий Побег!":
            $ alt_day2_us_escape = True
        "Что я, псих - с мелкой бегать?":
            $ alt_day2_us_escape = False
    menu:
        "Стыдно, но в Д1 запсиховали, проснувшись посреди лета":
            $ semen_panique = True
        "Сэм - нитакой!":
            $ semen_panique = False
    menu:
        "Проспал утром":
            jump alt_day6_true_CS_talk_short
        "Был паинькой и поднялся сразу":
            menu:
                "В Д2 вступил в клуб кибернетиков":
                    $ alt_day2_club_join_cyb = True
                "НЕТ! Кибернетики - опасные психи!":
                    $ alt_day2_club_join_cyb = False
            jump alt_day6_true_CS_talk
#
label alt_day6_true_beach_debug:
    menu:
        "в Д1 Славя отвела от ворот до домика ОД":
            $ alt_day1_sl_conv = True
        "в Д1 Славя шли от ворот сами и вышли на пристань":
            $ alt_day1_sl_conv = False
    menu:
        "в Д2 видели, как купается Славя":
            $ alt_day2_date = 2
        "В Д2 замутили было с Алисой (флаг свидания и плавки в придачу)":
            $ alt_day2_date = 3
        "Тян не нужны.":
            $ alt_day2_date = 0
    menu:
        "Был пляж в Д5":
            $ alt_uvao_D5_evening_sl = True
        "Не было пляжа в Д5":
            $ alt_uvao_D5_evening_sl = False
    menu:
        "В Д6 проспал утром":
            $ alt_uvao_D6_CS_vetrov = False
        "В Д6 был паинькой и поднялся сразу":
            $ alt_uvao_D6_CS_vetrov = True
    jump alt_day6_true_beach

label alt_day6_lunch_dv_sl_debug:
    $ alt_uvao_D5_hentai = False
    menu:
        "Быстрый переход к отладке полной беседы с Алисой":
            $ alt_uvao_true = True
            $ alt_uvao_D5_sh_mines = False
            $ alt_day1_sl_conv = False
            $ alt_uvao_D4_lunch_un = True
            $ alt_uvao_D4_lunch_sl = False
            $ alt_uvao_D5_evening_sl = False
            $ alt_uvao_D5_evening_dv_un = True
            $ alt_uvao_D6_CS_vetrov = True
        "Не-е-ет, я хочу помучиться с установкой флагов!":
            menu:
                "в Д1 Славя отвела от ворот до домика ОД":
                    $ alt_day1_sl_conv = True
                "в Д1 Славя шли от ворот сами и вышли на пристань":
                    $ alt_day1_sl_conv = False
            menu:
                "Идём по тру-ветке":
                    $ alt_uvao_true = True
                "В Д4 соскочили с Виолы и пришли на обед с хозработ":
                    $ alt_uvao_true = False
            if (not alt_uvao_true):
                menu:
                    "В Д5 обедали в столовой":
                        $ alt_uvao_D5_sh_mines = False
                    "В Д5 шарились по шахтам":
                        $ alt_uvao_D5_sh_mines = True
            menu:
                "Обедали в Д4 с Леной":
                    $ alt_uvao_D4_lunch_un = True
                    $ alt_uvao_D4_lunch_sl = False
                "Обедали в Д4 со Славей":
                    $ alt_uvao_D4_lunch_un = False
                    $ alt_uvao_D4_lunch_sl = True
                "Обедали в Д4 в одиночестве":
                    $ alt_uvao_D4_lunch_un = False
                    $ alt_uvao_D4_lunch_sl = False
            menu:
                "Вечером Д5 ходили на пляж":
                    $ alt_uvao_D5_evening_sl = True
                    $ alt_uvao_D5_evening_dv_un = False
                "Вечером Д5 ходили на площадь":
                    $ alt_uvao_D5_evening_sl = False
                    $ alt_uvao_D5_evening_dv_un = True
                "Вечером Д5 шлялись где-то ещё":
                    $ alt_uvao_D5_evening_sl = False
                    $ alt_uvao_D5_evening_dv_un = False
            if alt_uvao_true:
                menu:
                    "В Д6 проспал утром":
                        $ alt_uvao_D6_CS_vetrov = False
                    "В Д6 был паинькой и поднялся сразу":
                        $ alt_uvao_D6_CS_vetrov = True
    jump alt_day6_lunch_dv_sl

label alt_day6_uvao_left_concert_time_debug:
    menu:
        "В Д6 говорили с Мику про Лену":
            $ alt_uvao_D6_left_MI_talk = True
        "В Д6 к Мику не попали":
            $ alt_uvao_D6_left_MI_talk = False
    # menu:
        # "В Д2 поддались обаянию Ули и совершили Великий Побег!":
            # $ alt_day3_duty = True
        # "Что я, псих - с мелкой бегать?":
            # $ alt_day3_duty = False
    # menu:
        # "В Д6 проспал утром":
            # $ alt_uvao_D6_CS_vetrov = False
        # "В Д6 был паинькой и поднялся сразу":
            # $ alt_uvao_D6_CS_vetrov = True
    jump alt_day6_uvao_left_concert_time

label alt_day6_uvao_left_aidpost_debug:
    menu:
        "В Д2 поддались обаянию Ули и совершили Великий Побег!":
            $ alt_day3_duty = True
        "Что я, псих - с мелкой бегать?":
            $ alt_day3_duty = False
    menu:
        "В Д6 проспал утром":
            $ alt_uvao_D6_CS_vetrov = False
        "В Д6 был паинькой и поднялся сразу":
            $ alt_uvao_D6_CS_vetrov = True
    jump alt_day6_uvao_left_aidpost
    
label scenario_uvao_sprites:
    menu:
        # "Спрайты veryfar":
            # label scenario_uvao_sprites_veryfar:
            
            # jump scenario_uvao_sprites
        "Электроник с плюхой":
            label scenario_uvao_sprites_el_slap:
            show el scared pioneer
            "!!!"
            show el pioneer slap
            "..."
            hide el
            jump scenario_uvao_sprites
        "Коллайдер-сама":
            label scenario_uvao_sprites_cs:
            menu:
                "close":
                    show cs normal close #ванильный спрайт. Почему-то упрыгивает влево
                    "cs normal close"
                    show cs normal2 close
                    "cs normal2 close"
                    show cs smile2 close
                    "cs smile2 close"
                    show cs badgirl2 close
                    "cs badgirl2 close"
                    show cs normal glasses_thr close
                    "cs normal glasses_thr close"
                    show cs fear glasses_thr close
                    "cs fear glasses_thr close"
                    show cs fear close
                    "cs fear close"
                    jump scenario_uvao_sprites_cs
                "normal":
                    show cs smile #ванильный спрайт
                    "cs smile"
                    show cs important
                    "cs important"
                    show cs smile2
                    "cs smile2"
                    show cs laugh
                    "cs laugh"
                    show cs laugh2
                    "cs laugh2"
                    show cs laugh3
                    "cs laugh3"
                    show cs doubt2
                    "cs doubt2"
                    show cs fear2
                    "cs fear2"
                    show cs normal glasses
                    "cs normal glasses"
                    show cs normal2 glasses_thr
                    "cs normal2 glasses_thr"
                    show cs smile2 glasses_thr
                    "cs smile2 glasses_thr"
                    show cs laugh2 glasses_thr
                    "cs laugh2 glasses_thr"
                    show cs fear2 glasses_thr
                    "cs fear2 glasses_thr"
                    show cs normal2 glasses_over
                    "cs normal2 glasses_over"
                    show cs smile2 glasses_over
                    "cs smile2 glasses_over"
                    show cs laugh2 glasses_over
                    "cs laugh2 glasses_over"
                    jump scenario_uvao_sprites_cs
                "far":
                    show cs fear far
                    "cs fear far"
                    jump scenario_uvao_sprites_cs
                "Назад":
                    hide cs
            jump scenario_uvao_sprites
        "Шурик":
            label scenario_uvao_sprites_sh_bar:
            menu:
                "close":
                    show sh rage pioneer close # ванильный спрайт
                    "sh rage pioneer close"
                    show sh angry bar close
                    "sh angry bar close"
                    show sh angry bar2 close
                    "sh angry bar2 close"
                    jump scenario_uvao_sprites_sh_bar
                "normal":
                    show sh rage pioneer # ванильный спрайт
                    "sh rage pioneer"
                    show sh angry bar
                    "sh angry bar"
                    show sh angry bar3
                    "sh angry bar3"
                    jump scenario_uvao_sprites_sh_bar
                "far":
                    show sh rage pioneer far# ванильный спрайт
                    "sh rage pioneer far"
                    show sh angry bar far
                    "sh angry bar far"
                    show sh angry bar3 far
                    "sh angry bar3 far"
                    jump scenario_uvao_sprites_sh_bar
                "veryfar":
                    show sh angry bar veryfar:
                        xalign 0.6 yalign 0.999 zoom 0.7
                    "Падай!"
                    show sh angry bar veryfar:
                        yanchor 1.0 xanchor 1.0 xalign 0.6 yalign 0.999 zoom 0.7 transform_anchor True
                        easeout 0.5 yanchor 1.0 xanchor 1.0 rotate -90.0
                    "..."
                    hide sh
                    jump scenario_uvao_sprites_sh_bar
                "Назад":
                    hide sh
            jump scenario_uvao_sprites
        "Мод-тян":
            label scenario_uvao_sprites_sh:
            show mt scared panama pioneer #ванильный спрайт
            "mt scared panama pioneer"
            show mt scared3 panama pioneer
            "mt scared3 panama pioneer"
            hide mt
            jump scenario_uvao_sprites
        "Мокрая Леночка":
            show un cry wet_dress
            "un cry wet_dress"
            show un cry_smile wet_dress
            "un cry_smile wet_dress"
            show un sad wet_dress
            "un sad wet_dress"
            show un scared wet_dress
            "un scared wet_dress"
            show un shocked wet_dress
            "un shocked wet_dress"
            show un surprise wet_dress
            "un surprise wet_dress"
            hide un
            jump scenario_uvao_sprites
        "Славя в 25":
            show sl 25 normal
            "sl 25 normal"
            show sl 25 normal far
            "sl 25 normal far"
            show sl 25 fear_1
            "sl 25 fear_1"
            show sl 25 fear_1 far
            "sl 25 fear_1 far"
            show sl 25 fear_2
            "sl 25 fear_2"
            show sl 25 fear_2 far
            "sl 25 fear_2 far"
            show sl 25 displeased
            "sl 25 displeased"
            show sl 25 displeased far
            "sl 25 displeased far"
            hide sl
            jump scenario_uvao_sprites
        "Назад":
            jump scenario_uvao_root_D4_debug

label scenario_uvao_bg:
    menu:
        "Смотрим мерцание огонька спички":
            # scene int_mine_crossroad_burning
            scene bg int_mine_crossroad: # Имя должно совпадать с указанным ниже
                contains: # это - фон, который надо показать
                    'bg int_mine_crossroad' with fade 
                contains: # это - оранжевенькая тонировка
                    'scenario_alt/Pics/matches_tone.png' 
                    additive 1.0
                contains: # это - дрожание пламени
                    'scenario_alt/Pics/matches_lightmask.png'
                    xalign 0.5 yalign 1.0 
                    function random_zoom
                    repeat
            
            "Спичка горит."
            scene black with fade2
            "Потухла"
            scene bg int_mine:
                contains: 
                    'bg int_mine' with fade 
                contains: 
                    'scenario_alt/Pics/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_alt/Pics/matches_lightmask.png'
                    xalign 0.5 yalign 1.0 
                    function random_zoom
                    repeat   
            "Как я сюда попал?"
            scene black with fade2
            "Ну-ка, еще одну спичку…"
            scene bg int_mine_halt:
                contains: 
                    'bg int_mine_halt' with fade 
                contains: 
                    'scenario_alt/Pics/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_alt/Pics/matches_lightmask.png'
                    xalign 0.5 yalign 1.0 
                    function random_zoom
                    repeat
            "Да что за фигня-то?!"
            scene black with fade2
            "И еще разок…"
            scene bg int_mine_door:
                contains: 
                    'bg int_mine_door' with fade 
                contains: 
                    'scenario_alt/Pics/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_alt/Pics/matches_lightmask.png'
                    xalign 0.5 yalign 1.0 
                    function random_zoom
                    repeat
            "Бред какой-то…"
            scene black with fade2
            "…"
            jump scenario_uvao_bg
        "Жжем спички в шахтах и ходим":
            scene int_mine_crossroad_matches
            $ renpy.music.play( (match_lights, silence), 'sound', True)
            "Идем себе, гуляем по шахтам…"
            "Спички жжем…"
            "Смеемся…"
            "А попадаются одни перекрестки!"
            "Кажется, я заблудился…"
            "Или я вообще с места не двигаюсь?"
            "Да ну нафиг!"
            "Блин…"
            "Хорошо, что спички в коробке не заканчиваются…"
            "Я уже и Шурику был бы рад!"
            "Да ну вас всех в жопу."
            scene black
            stop sound
            jump scenario_uvao_bg
        "Назад":
            jump scenario_uvao_root_D4_debug            
#    scene black with fade2
#    return
