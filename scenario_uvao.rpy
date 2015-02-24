
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
    $ uvao_D4_aidpost_visit = False
# Флаг попадания с обеда на концерт
    $ uvao_D4_concert = False
# Флаг рассказа Слави про Генду за обедом
    $ uvao_D4_sl_genda_tale = False
    jump scenario_uvao_root_D4
   
   
label scenario_uvao_root_D4:
#
    menu:
        "Отладка: Сразу Д4-Обед":
            call uvao_uvao_D4_lunch
        "Отладка: Сразу Д4-встреча с Юлей после обеда без концерта":
            call uvao_D4_meet_Yulia_after_lunch
        "Отладка: Сразу Д4-встреча с Юлей после ужина":
            call uvao_D4_meet_Yulia_at_evening
        "Отладка: Утро от пробуждения по завтрак":
            jump alt_day4_start_uvao
        "Отладка: Уборка гирлянд":
            call uvao_D4_garlands_removal
#        "Прохождение Д4 по порядку":
#            $ alt_chapter(4, u"Обед")
#            call uvao_uvao_D4_lunch
#
#            if uvao_D4_concert:
#                $ alt_chapter(4, u"Концерт после обеда")
#                th "Ой, концерт забыли!"
#                th "И Юлю я не встретил...!"
#            else:
#                $ alt_chapter(4, u"После обеда без концерта")
#                call uvao_D4_meet_Yulia_after_lunch
#
    $ renpy.pause (1)
    scene black with fade2
    return
