
init:
    $ mods["scenario_uvao"] = u"ЮВАО рут - отладка"
    $ config.developer = True
    $ herc = False
    $ loki = False

    $ th_prefix = "«"
    $ th_suffix = "»"
    
    $ mod_tags["scenario_uvao"] = ["length:days","gameplay:vn","protagonist:male","special:TODO","character:Виола","character:Алиса","character:Электроник","character:Семён","character:Мику","character:Ольга Дмитриевна","character:Женя","character:Пионер","character:Шурик","character:Славя","character:Лена","character:Ульяна","character:Юля"]
    $ routetag = "uvao"
label scenario_uvao:
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
    $keys_keep = True
    $keys_take = 1
    $dv_help = True
#
    jump scenario_uvao_root_D4
   
   
label scenario_uvao_root_D4:
#
    menu:
        "Отладка: Встреча Юли в д3":
            call alt_day3_meet_uvao
        "Прохождение Д4 по порядку":
            jump alt_day4_start_uvao
#        "Отладка: Утро от пробуждения по завтрак":
#            jump alt_day4_start_uvao
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
        "Отладка: Сразу Д4-ужин 100% без Виолы":
            $ alt_day4_uv_viola_morning = False
            jump uvao_uvao_D4_supper
        "Отладка: Сразу Д4-встреча с Юлей после ужина":
            jump uvao_D4_meet_Yulia_at_evening
        "Отладка: Сразу Д4-хождения перед сном после ужина с Виолой":
            $ uvao_D4_supper_cs = True
            jump uvao_D4_evening_business
        "Отладка: Сразу Д4-хождения перед сном после ужина без Виолы":
            $ uvao_D4_supper_cs = False
            jump uvao_D4_evening_business
    $ renpy.pause (1)
    jump scenario_uvao_root_D4
#    scene black with fade2
#    return
