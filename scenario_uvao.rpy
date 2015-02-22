
init:
    $ mods["scenario_uvao"] = u"ЮВАО рут - demo"
    $ herc = False
    $ loki = False
    
    $ mod_tags["scenario_uvao"] = ["length:days","gameplay:vn","protagonist:male","special:TODO","character:Виола","character:Алиса","character:Электроник","character:Семён","character:Мику","character:Ольга Дмитриевна","character:Женя","character:Пионер","character:Шурик","character:Славя","character:Лена","character:Ульяна","character:Юля"]
#    $ alt_prologue = False
    $ routetag = "uvao"
label scenario_uvao:
    $ make_names_known()
#    $ prolog_time()
    $ set_mode_adv()
    jump scenario_uvao_root_D4

label scenario_uvao_root_D4:
#    $ backdrop = "epilogue"
    $ alt_chapter(4, u"После обеда")

    call uvao_D4_meet_Yulia_after_lunch

    $ renpy.pause (1)
    scene black with fade2
    return