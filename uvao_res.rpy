init python:
    # Кусок кода для заставок по мере продвижения. надо вставить в alt_chapter автора
    def alt_chapter_uv (day_number, chapter_name) :
        renpy.block_rollback()
        renpy.scene()
        renpy.show('bg ext_stand_2')
        renpy.pause(1.0)
        renpy.transition(dissolve)
    
    
        if routetag == "uv_unknown": #Кошочку еще не знаем
            renpy.show("uv black silhouette", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        if routetag == "uv": #Кошонка-распашонка
            renpy.show("uv normal", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        if routetag == "uv_true": #Кошочка поражена происходящим
            renpy.show("uv surprise", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        if routetag == "uv_false": #Кошонка на позитиве
            renpy.show("uv grin", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        if routetag == "uv_bad": #Виноватая кошонка
            renpy.show("uv guilty", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
            
        dn = (u"7ДЛ:День %d") % (day_number)
        sdn = (u"7ДЛ:День %d") % (day_number)
        save_name = ((sdn) + (u" - ")) + (chapter_name)

        renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.35))
        renpy.show('day_text', what=Text(chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.45))

        renpy.pause(3)
        renpy.scene()
        renpy.show('bg black')
        renpy.transition(dissolve)
        set_mode_adv()
        
    # Функция для дрожания огонька спички
    def random_zoom(trans, st, at):
        if st < 1.0: # 1 sec random zooming each 0.1 sec
            trans.zoom = 1.0 + renpy.random.random() * 0.5 
            return 0.1
        trans.zoom = 1.0
        return None
        
init:

#bg:
#    image ext_dining_hall_away_night_uvao1 = "scenario_uvao/images/ext_dining_hall_away_night_uvao1.jpg"
#    image ext_dining_hall_away_night_uvao2 = "scenario_uvao/images/ext_dining_hall_away_night_uvao2.jpg"
    #ext's
    image ext_old_building_day = "scenario_uvao/images/ext_old_building_day.jpg"
    
    #int's
    image int_old_building_day_uvao = "scenario_uvao/images/int_old_building_day_uvao.jpg"
    image int_mines_halt_spotlight = "scenario_uvao/images/int_mines_halt_spotlight.jpg"
    image int_catacombs_entrance_light = "scenario_uvao/images/int_catacombs_entrance_light.jpg"
    image int_old_building_day_uvao = "scenario_uvao/images/int_old_building_day_uvao.jpg"
    # анимация перекрестка с зажиганием спичек
    image int_mine_crossroad_matches: 
        "bg black" with fade2
        0.5
        block:
            block:
                contains: 
                    'bg int_mine_crossroad' with fade2 
                contains: 
                    'scenario_uvao/images/matches_tone.png' 
                    additive 1.0
                contains: 
                    'scenario_uvao/images/matches_lightmask.png'
                    xalign 0.5 yalign 1.0 
                    function random_zoom
                    repeat            
            4.0
            "bg black" with fade2
            4.0
            repeat
                   
#cg
#    image pioner_lib_hiding = "scenario_uvao/images/pioner_lib_hiding.jpg"
    image uv_photo_city = "scenario_uvao/images/uv_photo_city.jpg"
    image uv_bunker_hentai = "scenario_uvao/images/uv_bunker_hentai.jpg"
    # Кошочка авторства Орики
    image uv_new_hentai1 = "images/1080/cg/epilogue_uv_hentai_1.jpg"
    image uv_new_hentai2 = "images/1080/cg/epilogue_uv_hentai_2.jpg"

#sprite alt_chapter
    image uv black silhouette = "scenario_uvao/images/uv_black.png"
    
#sounds
    $ phone_vibro = "scenario_uvao/sounds/vibration-smartphone.ogg"
    $ match_lights ="scenario_uvao/sounds/lighting-a-match.ogg"
    $ silence = "scenario_uvao/sounds/silence_4sec.ogg"
