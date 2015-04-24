init:
    $ style.alt_days = Style(style.default)
    $ style.alt_days.color = "#390874"
    $ style.alt_days.italic = False
    $ style.alt_days.bold = True
    $ style.alt_days.size = 64
    $ style.alt_days.text_align = 0.5

    $ style.alt_chapters = Style(style.default)
    $ style.alt_chapters.color = "#2572ff"
    $ style.alt_chapters.italic = False
    $ style.alt_chapters.bold = True
    $ style.alt_chapters.size = 48
    $ style.alt_chapters.text_align = 0.5

init python:
    def alt_chapter(day_number, chapter_name):
        global save_name
        renpy.block_rollback()
        renpy.scene()
        renpy.show('bg ext_stand_2')
        renpy.pause(1.0)
        renpy.transition(dissolve)
        
        if routetag == "dv": #Классическая и диджей ветка гуд
            renpy.show("dv normal pioneer2", at_list=[left])
            renpy.transition(moveinleft)
        elif routetag == "dvbad": #Классическая ветка, бэд, диджей ветка дисмисс
            renpy.show("dv sad pioneer2", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)    
           
        elif routetag == "dv7dl": #7дл-ветка, гуд
            renpy.show("dv normal pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "dv7dlbad": #7дл-ветка, реджект/дисмисс
            renpy.show("dv guilty pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)

        elif routetag == "mi7dl": #7дл-ветка, диджей гуд
            renpy.show("mi normal pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "mi7": #Мику-коммон
            renpy.show("mi sad pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "mi7dlbad": #7дл-ветка, реджект, диджей нейтрал
            renpy.show("mi cry pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "mi7dlgood": #7дл-ветка, реджект, диджей нейтрал
            renpy.show("mi happy pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "mi7rej": #7дл-ветка, реджект, диджей бэд
            renpy.show("mi serious pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "mi7true": #7дл-ветка, реджект, диджей бэд
            renpy.show("mi shy pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
            
        elif routetag == "sl": #Классическая ветка гуд
            renpy.show("sl normal pioneer", at_list=[left])
            renpy.transition(moveinleft)
        elif routetag == "slbad": #Классическая ветка, бэд
            renpy.show("sl cry pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)    
            
        elif routetag == "sl7dl": #7дл-ветка, гуд
            renpy.show("sl smile pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "sl7dlbad": #7дл-ветка, дисмисс
            renpy.show("sl cry pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        
        elif routetag == "un": #Классическая
            renpy.show("un normal pioneer2", at_list=[left])
            renpy.transition(moveinleft)
        elif routetag == "unbad": #Классическая ветка, бэд
            renpy.show("un sad pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)    
            
        elif routetag == "un7dl": #7дл-ветка, гуд
            renpy.show("un normal pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "un7dlbad": #7дл-ветка, реджект/бэд
            renpy.show("un cry pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "un7dlgood": #7дл-ветка, реджект/бэд
            renpy.show("un cry_smile pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
            
        elif routetag == "mt7dl": #7дл-ветка, гуд
            renpy.show("mt grin pioneer", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
            
        elif routetag == "uv_unknown": #Кошочку еще не знаем
            renpy.show("uv black silhouette", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "uv": #Кошонка-распашонка
            renpy.show("uv normal", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "uv_true": #Кошочка поражена происходящим
            renpy.show("uv surprise", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "uv_false": #Кошонка на позитиве
            renpy.show("uv grin", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
        elif routetag == "uv_bad": #Виноватая кошонка
            renpy.show("uv guilty", at_list=[left])
            renpy.transition(moveinleft)
            renpy.pause(2.0)
            
        else:
            renpy.show("owl")
            renpy.pause(0.3)
        
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

    if persistent.altCardsDemo == None:
        persistent.altCardsDemo = False

    if persistent.altCardsFail == None:
        persistent.altCardsFail = False

    if persistent.altCardsWon1 == None:
        persistent.altCardsWon1 = False

    if persistent.altCardsWon2 == None:
        persistent.altCardsWon2 = False

    if persistent.altCardsWon3 == None:
        persistent.altCardsWon3 = False
        
    if persistent.altCardsWon4 == None:
        persistent.altCardsWon4 = False
    
    
    # Функция для дрожания огонька спички в котокомбах
    def random_zoom(trans, st, at):
        if st < 1.0: # 1 sec random zooming each 0.1 sec
            trans.zoom = 1.0 + renpy.random.random() * 0.5 
            return 0.1
        trans.zoom = 1.0
        return None        

    # Фабрика спрайтов (Provided by UVAO)
    # Константы:
    # тонировка:
    tint_night = im.matrix.tint(0.63, 0.78, 0.82)
    tint_sunset = im.matrix.tint(0.94, 0.82, 1.0)    
    # Дефолтный путь к спрайтам
    _default_sprites_path = 'scenario_alt/Pics/sprites'

    # Простая функция, строит спрайт из переданных путей
    def ComposeSprite(*argv):
        #строим аргументы для im.Composite
        subargs = list()
        for arg in argv:
           subargs.append( (0,0) )
           subargs.append( arg )
        sprite = im.Composite(None, *subargs)
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite, tint_night), True, sprite)
    # /ComposeSprite(*argv)
        
    # Функция, собирающая спрайты из запчастей
    # types - набор калибров спрайтов. Любой набор из ('far', 'close', 'normal', 'veryfar'). По пути, где лежат спрайты, должны быть соотвествующие директории, иначе не найдет
    # argv - файлы-запчасти. передаются в формате ('path', 'file') - например ('images/1080/sprites/','dv/dv_1_coat.png'), или просто 'file' - тогда используется _default_sprites_path
    # на выходе - dict спрайтов, по одному для каждого из types
    def ComposeSpriteSet(distance, *argv):
        if isinstance(distance, str): #если types содержит только один параметр.
            distances = (distance,) # 1-tuple. Иначе for будет перебирать символы в строке.
        else:
            distances = distance
        ret = dict()    
        for dst in distances:
            #строим аргументы для ComposeSprite
            subargs = list()
            for arg in argv:
                if isinstance(arg, str): #просто file
                    subarg = (_default_sprites_path, arg)
                else: # (path, file)
                    subarg = arg;
                subargs.append( subarg[0] + '/' + dst +'/' + subarg[1] ) # 'images/1080/sprites/normal/dv/dv_1_coat.png'
            ret[dst] = ComposeSprite(*subargs)
        return ret
    # /ComposeSpriteSet(type, *argv)    
    
init 52 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["chibi"] = None
        
init -1001 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["map_chibi"] = None
            
init -999 python:
    def get_image_7dl(file):
        return "scenario_alt/Pics/%s" % (file)
        
init -997 python:
        
    store.map_pics = {
            "widget map": get_image_7dl("gui/maps/map_bg.jpg"),
            "bgpic": get_image_7dl("gui/maps/map_bg.jpg"),
            "bg map": get_image_7dl("gui/maps/map_bg.jpg"),
            "avaliable": get_image_7dl("gui/maps/map_avaliable.jpg"),
            "selected": get_image_7dl("gui/maps/map_selected.jpg")
        }
    
    store.map_zones = {
                "un_mi_house":   {"position":[804,146,853,203],"default_bg":bg_tmp_image(u"Лена и Мику")},
                "sl_mz_house":   {"position":[1020,243,1079,309],"default_bg":bg_tmp_image(u"Славя и Женя")},
                "el_sh_house":   {"position":[843,283,891,340],"default_bg":bg_tmp_image(u"Эл и Шурик")},
                "dv_us_house":   {"position":[711,615,768,674],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
                "shed":          {"position":[1148,489,1215,583],"default_bg":bg_tmp_image(u"Склад")},
                "old_house":     {"position":[228,993,347,1080],"default_bg":bg_tmp_image(u"Старый корпус")},
        }
    
    store.map_chibi = {
            "?" : get_image_7dl("gui/maps/map_icon_n00.png"),
            "me": get_image_7dl("gui/maps/map_icon_n01.png"),
            "mi": get_image_7dl("gui/maps/map_icon_n02.png"),
            "sh": get_image_7dl("gui/maps/map_icon_n03.png"),
            "el": get_image_7dl("gui/maps/map_icon_n04.png"),
            "mz": get_image_7dl("gui/maps/map_icon_n05.png"),
            "mt": get_image_7dl("gui/maps/map_icon_n06.png"),
            "uv": get_image_7dl("gui/maps/map_icon_n07.png"),
            "un": get_image_7dl("gui/maps/map_icon_n08.png"),
            "us": get_image_7dl("gui/maps/map_icon_n09.png"),
            "dv": get_image_7dl("gui/maps/map_icon_n10.png"),
            "sl": get_image_7dl("gui/maps/map_icon_n11.png"),
            "cs": get_image_7dl("gui/maps/map_icon_n12.png"),
        }