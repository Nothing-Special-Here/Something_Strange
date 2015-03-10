
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

# приходит из Д1
    $ keys_keep = True
    $ keys_take = 1
    $ dv_help = 1
#
# приходит из Пролога ("пойду за тобой")
    $ alt_prologue = True
#
   
label scenario_uvao_root_D4_demo:
    scene anim prolog_1 
    with fade3
    window show
    show uvao_d1 at left 
    dreamgirl "Ты пойдёшь со мной?"
    menu:
        "Пойду, милая.":
            $ alt_prologue = True
        "Нет, я останусь здесь":
            $ alt_prologue = False

    dreamgirl "А ключи брать будем?"
    menu:
        "Возьму":
            $ keys_keep = True
            $ keys_take = 1     
            dreamgirl "Может, еще Алисе поможем?"
            menu:
                "Поможем":
                    $ dv_help = 1
                "Не-а":
                    $ dv_help = 0
        "Обойдусь без ключей":
            $ keys_keep = False
            $ keys_take = 0  
            
    hide uvao_d1

    menu:
        "Прохождение Д4 по порядку":
            call alt_day4_uvao_start
    $ renpy.pause (1)
    
    dreamgirl "А теперь еще раз!"
    jump scenario_uvao_root_D4_demo
#    scene black with fade2
#    return
