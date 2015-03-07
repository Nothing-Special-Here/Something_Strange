
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
    $ alt_day4_uv_viola_morning = False
# Флаг попадания с обеда на концерт
    $ uvao_D4_concert = False
# Флаг обеда с Леной 
    $ uvao_D4_lunch_un = False
# Флаг обеда со Славей
    $ uvao_D4_lunch_sl = False
# Флаг ужина с Виолой uvao_D4_supper_cs
    $ uvao_D4_supper_cs = False
#
# приходит из Д1
    $ keys_keep = True
    $ keys_take = 1
    $ dv_help = 1
#
# приходит из Пролога ("пойду за тобой")
    $ alt_prologue = True
#
    jump scenario_uvao_root_D4_debug
   
label scenario_uvao_root_D4_debug:

    menu:
        "Отладка: Встреча Юли в д3":
            call alt_day3_meet_uvao
        "Прохождение Д4 по порядку":
            jump alt_day4_start_uvao
        "Отладка: Уборка гирлянд":
            jump uvao_D4_garlands_removal_debug
        "Отладка: Посещение библиотеки":
            jump uvao_D4_library
        "Отладка: Сразу Д4-Обед":
            jump uvao_uvao_D4_lunch
        "Отладка: Сразу Д4-встреча с Юлей после обеда без концерта":
            $ uvao_D4_concert = False
            jump uvao_D4_meet_Yulia_after_lunch
        "Отладка: Сразу Д4-встреча с Юлей после концерта (обедали со Славей)":
            $ uvao_D4_concert = True
            $ uvao_D4_lunch_un = False
            $ uvao_D4_lunch_sl = True
            jump uvao_D4_meet_Yulia_after_lunch
        "Отладка: Сразу Д4-встреча с Юлей после концерта (обедали с Леной)":
            $ uvao_D4_concert = True
            $ uvao_D4_lunch_un = True
            $ uvao_D4_lunch_sl = False
            jump uvao_D4_meet_Yulia_after_lunch
        "Отладка: Сразу Д4-ужин с Виолой (на выбор)":
            $ alt_day4_uv_viola_morning = True
            jump uvao_uvao_D4_supper
        "Отладка: Сразу Д4-ужин без Виолы":
            $ alt_day4_uv_viola_morning = False
            jump uvao_uvao_D4_supper
        "Отладка: Сразу Д4-встреча с Юлей после ужина":
            jump uvao_D4_meet_Yulia_at_evening
        "Отладка: Сразу Д4-после ужина с Виолой":
            $ uvao_D4_supper_cs = True
            jump uvao_D4_evening_business
        "Отладка: Сразу Д4-после ужина без Виолы":
            $ uvao_D4_supper_cs = False
            jump uvao_D4_evening_business
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
                    "Выход":
                        pass
    $ renpy.pause (1)
    jump scenario_uvao_root_D4_debug
#    scene black with fade2
#    return
