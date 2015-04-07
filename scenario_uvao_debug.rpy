
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
            jump alt_day4_uvao_start
        "Отладка Д4":
            menu:
                "Отладка: Уборка гирлянд":
                    jump alt_day4_uvao_garlands_removal_debug
                "Отладка: Посещение библиотеки":
                    jump alt_day4_uvao_library
                "Отладка: Сразу Д4-Обед":
                    jump alt_day4_uvao_lunch
                "Отладка: Сразу Д4-встреча с Юлей после обеда без концерта":
                    $ alt_uvao_D4_concert = False
                    jump alt_day4_uvao_meet_Yulia_after_lunch
                "Отладка: Сразу Д4-встреча с Юлей после концерта (обедали со Славей)":
                    $ alt_uvao_D4_concert = True
                    $ alt_uvao_D4_lunch_un = False
                    $ alt_uvao_D4_lunch_sl = True
                    jump alt_day4_uvao_meet_Yulia_after_lunch
                "Отладка: Сразу Д4-встреча с Юлей после концерта (обедали с Леной)":
                    $ alt_uvao_D4_concert = True
                    $ alt_uvao_D4_lunch_un = True
                    $ alt_uvao_D4_lunch_sl = False
                    jump alt_day4_uvao_meet_Yulia_after_lunch
                "Отладка: Сразу Д4-ужин с Виолой (на выбор)":
                    $ alt_uvao_D4_viola_morning = True
                    jump alt_day4_uvao_supper
                "Отладка: Сразу Д4-ужин без Виолы":
                    $ alt_uvao_D4_viola_morning = False
                    jump alt_day4_uvao_supper
                "Отладка: Сразу Д4-встреча с Юлей после ужина":
                    jump alt_day4_uvao_meet_Yulia_at_evening
                "Отладка: Сразу Д4-после ужина с Виолой":
                    $ alt_uvao_D4_supper_cs = True
                    jump alt_day4_uvao_evening_business
                "Отладка: Сразу Д4-после ужина без Виолы":
                    $ alt_uvao_D4_supper_cs = False
                    jump alt_day4_uvao_evening_business
                "Назад":
                    jump scenario_uvao_root_D4_debug
        "Отладка Д5":
            menu:
                "Отладка: Подъём без доклада Виоле в Д4":
                    $ alt_uvao_true = False
                    jump alt_day5_uvao_getting_up
                "Отладка: Подъём с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_getting_up
                "Отладка: Спуск в бункер с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_tunnel                
                "Отладка: Спуск в бункер без доклада Виоле в Д4":
                    jump alt_day5_uvao_tunnel
                "Отладка: В бункере с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_bunker_debug                
                "Отладка: В бункере без доклада Виоле в Д4":
                    jump alt_day5_uvao_bunker_debug
                "Отладка: Поход наверх. Тру рут":
                    jump alt_day5_uvao_true_back
                "Отладка: Охота на Шурика в шахтах":
                    jump alt_day5_uvao_mines_sh
                "Отладка: Обед без доклада Виоле в Д4":
                    $ alt_uvao_true = False
                    jump alt_day5_uvao_lunch
                "Отладка: Обед с докладом Виоле в Д4":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_lunch
                "Отладка: Совместная охота на дикого Шурика not-uvao_true":
                    $ alt_uvao_true = False
                    jump alt_day5_capture_sh_together_debug
                "Отладка: Совместная охота на дикого Шурика uvao_true":
                    $ alt_uvao_true = True
                    jump alt_day5_capture_sh_together_debug
                "Отладка: Вечер not-uvao_true":
                    $ alt_uvao_true = False
                    jump alt_day5_uvao_evening_debug
                "Отладка: Вечер uvao_true":
                    $ alt_uvao_true = True
                    jump alt_day5_uvao_evening_debug
                "Назад":
                    jump scenario_uvao_root_D4_debug
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
