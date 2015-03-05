
init:
    $ mods["scenario_uvao_demo"] = u"ЮВАО рут - demo"
    $ config.developer = True
    $ herc = False
    $ loki = False

    $ th_prefix = "«"
    $ th_suffix = "»"
    
    $ mod_tags["scenario_uvao_demo"] = ["length:days","gameplay:vn","protagonist:male","special:TODO","character:Виола","character:Алиса","character:Электроник","character:Семён","character:Мику","character:Ольга Дмитриевна","character:Женя","character:Пионер","character:Шурик","character:Славя","character:Лена","character:Ульяна","character:Юля"]
    $ routetag = "uvao"
label scenario_uvao_demo:
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
    jump scenario_uvao_root_D4_demo
   
label scenario_uvao_root_D4_demo:

    menu:
        "Прохождение Д4 по порядку":
            jump alt_day4_start_uvao
    $ renpy.pause (1)
    jump scenario_uvao_root_D4_demo
#    scene black with fade2
#    return
