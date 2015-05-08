
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
    $ make_names_known()
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

#
# приходит из Д1
    $ keys_keep = True
    $ keys_take = 1
    $ dv_help = 1
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
                        "Палевная ветка (Ещё не готово)":
                            pass
                        "Беспалевная ветка":
                            jump alt_day6_uvao_duty
        "Картинки при смене глав":
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
                "normal":
                    show cs smile #ванильный спрайт
                    "cs smile"
                    show cs smile2
                    "cs smile2"
                    jump scenario_uvao_sprites_cs
                "close":
                    show cs normal close #ванильный спрайт. Почему-то упрыгивает влево
                    "cs normal close"
                    show cs normal2 close
                    "cs normal2 close"
                    show cs smile2 close
                    "cs smile2 close"
                    show cs badgirl2 close
                    "cs badgirl2 close"
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
                    'scenario_uvao/images/matches_tone.png' 
                    additive 1.0
                contains: # это - дрожание пламени
                    'scenario_uvao/images/matches_lightmask.png'
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
                    'scenario_uvao/images/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_uvao/images/matches_lightmask.png'
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
                    'scenario_uvao/images/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_uvao/images/matches_lightmask.png'
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
                    'scenario_uvao/images/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_uvao/images/matches_lightmask.png'
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
