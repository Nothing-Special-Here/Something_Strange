init:
#bg:
#    image ext_dining_hall_away_night_uvao1 = "scenario_uvao/images/ext_dining_hall_away_night_uvao1.jpg"
#    image ext_dining_hall_away_night_uvao2 = "scenario_uvao/images/ext_dining_hall_away_night_uvao2.jpg"

#cg
#    image pioner_lib_hiding = "scenario_uvao/images/pioner_lib_hiding.jpg"

#sprites
    image uv black silhouette = "scenario_uvao/images/uv_black.png"
    
init python:
    # Кусок кода для заставок по мере продвижения. надо вставить в alt_chapter автора
    def alt_chapter_uv () :
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
