init python:
# Константы:
    # тонировка:
    tint_night = im.matrix.tint(0.63, 0.78, 0.82)
    tint_sunset = im.matrix.tint(0.94, 0.82, 1.0)    
    # Дефолтный путь к спрайтам
    _default_sprites_path = 'scenario_uvao/images/sprites'

    # Функция, собирающая спрайты из запчастей
    # argv - файлы-запчасти под 3500
    # на выходе - 3 спрайта: far, close normal
    # def ComposeSprite( *argv):
        # Множитель для разных размеров
        # factor_close = 0.75
        # factor_normal = 0.6
        # factor_far = 0.45
        # factor_veryfar = 0.3333
        # тонировка:
        # tint_night = im.matrix.tint(0.63, 0.78, 0.82)
        # tint_sunset = im.matrix.tint(0.94, 0.82, 1.0)
        # строим аргументы для im.Composite
        # subargs = list()
        # for arg in argv:
           # subargs.append( (0,0) )
           # subargs.append( arg )
        # собраный спрайт 1500х3500
        # large_sprite =  im.Composite(None, *subargs)
        # ресайз и кроп под far, normal, close
        # sprite_close    = im.Crop(im.FactorScale(large_sprite, factor_close),   0, 0, 1125, 1080)
        # sprite_norm     = im.Crop(im.FactorScale(large_sprite, factor_normal),  0, 0, 900, 1080)
        # sprite_far      = im.Crop(im.FactorScale(large_sprite, factor_far),     0, 0, 675, 1080)
        # sprite_veryfar  = im.Crop(im.FactorScale(large_sprite, factor_veryfar), 0, 0, 450, 1080)
        # добавляем тонировку через ConditionSwitch
        # return {
            # 'far': ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite_far, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite_far, tint_night), True, sprite_far),
            # 'normal': ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite_norm, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite_norm, tint_night), True, sprite_norm), 
            # 'close': ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite_close, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite_close, tint_night), True, sprite_close),
            # 'veryfar': ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite_veryfar, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite_veryfar, tint_night), True, sprite_veryfar)
        # }
   
    # Функция, собирающая спрайты из запчастей
    # types - набор калибров спрайтов. ('far', 'close', 'normal',...)
    # argv - файлы-запчасти под 3500
    # на выходе - 3 спрайта: far, close, normal,...
    def ComposeSpriteEx(types, *argv):
        # Множитель для разных размеров
        factors = {'veryfar':0.3333, 'far':0.45, 'normal':0.6, 'close':0.75}
        # тонировка:
        tint_night = im.matrix.tint(0.63, 0.78, 0.82)
        tint_sunset = im.matrix.tint(0.94, 0.82, 1.0)
        #строим аргументы для im.Composite
        subargs = list()
        for arg in argv:
           subargs.append( (0,0) )
           subargs.append( arg )
        # собраный спрайт 1500х3500
        large_sprite =  im.Composite(None, *subargs)
        
        # формируем возвращаемый набор:
        ret = dict()
        if isinstance(types, str): #если types содержит только один параметр.
            sprite = im.Crop(im.FactorScale(large_sprite, factors[types]), (0, 0, factors[types]*1500, 1080))
            ret[types] = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite, tint_night), True, sprite)
        else: # если в types несколько параметров
            for key in types:
                sprite = im.Crop(im.FactorScale(large_sprite, factors[key]), (0, 0, factors[key]*1500, 1080))
                ret[key] = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite, tint_night), True, sprite)
        return ret
        
    # Простая функция, строит спрайт из переданных путей
    def ComposeSprite(*argv):
        #строим аргументы для im.Composite
        subargs = list()
        for arg in argv:
           subargs.append( (0,0) )
           subargs.append( arg )
        sprite = im.Composite(None, *subargs)
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite, tint_night), True, sprite)
    # ComposeSprite(*argv)
        
    # Функция, собирающая спрайты из запчастей
    # types - набор калибров спрайтов. ('far', 'close', 'normal',...)
    # argv - файлы-запчасти. передаются в формате ('path', 'file') - например ('images/1018/sprites/','dv/dv_1_coat.png'), или просто 'file' - тогда используется _default_sprites_path
    # на выходе - dict спрайтов, по одному для каждого types
    #
    def ComposeSpriteSet(distance, *argv):
        
        if isinstance(distance, str): #если types содержит только один параметр.
            distances = (distance,) # 1-tuple
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
                subargs.append( subarg[0] + '/' + dst +'/' + subarg[1] ) # 'images/1018/sprites/normal/dv/dv_1_coat.png'
            ret[dst] = ComposeSprite(*subargs)
        return ret
    # ComposeSpriteSet(type, *argv)
    
init:

#####################################################    
# спрайты, с тонировкой под закат или ночь
#####################################################
    $ _uvao_spr = 'scenario_uvao/images/sprites'
    #sl
    $ _sl_pioneer_normal = ComposeSpriteSet('veryfar', 'sl/sl_1_body.png', 'sl/sl_1_pioneer.png', 'sl/sl_1_normal.png')
    image sl pioneer normal veryfar = _sl_pioneer_normal['veryfar']
    $ _sl_pioneer_serious = ComposeSpriteSet('veryfar', 'sl/sl_1_body.png', 'sl/sl_1_pioneer.png', 'sl/sl_1_serious.png')
    image sl pioneer serious veryfar = _sl_pioneer_serious['veryfar']
    $ _sl_pioneer_scared = ComposeSpriteSet('veryfar', 'sl/sl_4_body.png', 'sl/sl_4_pioneer.png', 'sl/sl_4_scared.png')
    image sl pioneer serious veryfar = _sl_pioneer_serious['veryfar']   
    
    #un
    $ _un_pioneer_normal = ComposeSpriteSet('veryfar', 'un/un_1_body.png', 'un/un_1_pioneer.png', 'un/un_1_normal.png')
    image un pioneer normal veryfar = _un_pioneer_normal['veryfar']
    $ _un_pioneer_scared = ComposeSpriteSet('veryfar', 'un/un_2_body.png', 'un/un_2_pioneer.png', 'un/un_2_scared.png')
    image un pioneer scared veryfar = _un_pioneer_scared['veryfar']
    $ _un_pioneer_shocked = ComposeSpriteSet('veryfar', 'un/un_2_body.png', 'un/un_2_pioneer.png', 'un/un_2_shocked.png')
    image un pioneer shocked veryfar = _un_pioneer_shocked['veryfar']    
    $ _un_pioneer_serious = ComposeSpriteSet('veryfar', 'un/un_3_body.png', 'un/un_3_pioneer.png', 'un/un_3_serious.png')
    image un pioneer serious veryfar = _un_pioneer_serious['veryfar']

    # el
    $ _el_pioneer_slap = ComposeSpriteSet('normal', 'el/el_2_body.png', 'el/el_2_pioneer.png',  'el/el_slap.png')
    # image el pioneer slap close = _el_pioneer_slap['close']
    image el pioneer slap       = _el_pioneer_slap['normal']
    # image el pioneer slap far   = _el_pioneer_slap['far']
    $ _el_pioneer_normal = ComposeSpriteSet('veryfar', 'el/el_1_body.png', 'el/el_1_pioneer.png',  'el/el_1_normal.png')
    image el pioneer normal veryfar = _el_pioneer_normal['veryfar']
    
    #sh
    $ _sh_pioneer_rage = ComposeSpriteSet('veryfar', 'sh/sh_2_body.png', 'sh/sh_2_rage.png')
    image sh pioneer rage veryfar = _sh_pioneer_rage['veryfar']
    $ _sh_angry_bar = ComposeSpriteSet(('far','normal','close'), 'sh/sh_angry_bar.png')
    image sh angry bar close        = _sh_angry_bar['close']
    image sh angry bar              = _sh_angry_bar['normal']
    image sh angry bar far          = _sh_angry_bar['far']
    $ _sh_angry_bar2 = ComposeSpriteSet( 'close',  'sh/sh_angry_bar2.png')
    image sh angry bar2 close    = _sh_angry_bar2['close']
    # image sh angry bar2          = _sh_angry_bar2['normal']
    # image sh angry bar2 far      = _sh_angry_bar2['far']   
    $ _sh_angry_bar3 = ComposeSpriteSet(('normal', 'far', 'veryfar'),  'sh/sh_angry_bar3.png')
    #image sh angry bar3 close   = _sh_angry_bar3['close']
    image sh angry bar3         = _sh_angry_bar3['normal']
    image sh angry bar3 far     = _sh_angry_bar3['far']
    image sh angry bar3 veryfar = _sh_angry_bar3['veryfar']

    # mt
    $ _mt_pioneer_angry = ComposeSpriteSet('veryfar',  'mt/mt_2_body.png', 'mt/mt_2_pioneer.png',  'mt/mt_2_angry.png')
    image mt pioneer angry veryfar  =_mt_pioneer_angry['veryfar']
    $ _mt_pioneer_normal = ComposeSpriteSet('veryfar', 'mt/mt_1_body.png',  'mt/mt_1_pioneer.png', 'mt/mt_1_normal.png')
    image mt pioneer normal veryfar  =_mt_pioneer_normal['veryfar']
    # $ _mt_pioneer_shock = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_shock.png')
    # image mt pioneer shock close    =_mt_pioneer_shock['close']
    # image mt pioneer shock          =_mt_pioneer_shock['normal']     
    # image mt pioneer shock far      =_mt_pioneer_shock['far'] 
    # $ _mt_pioneer_shock_panama = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_shock.png', 'images/3500/sprites/full/mt/mt_3_panama.png')
    # image mt pioneer shock panama close   =_mt_pioneer_shock_panama['close']
    # image mt pioneer shock panama         =_mt_pioneer_shock_panama['normal']     
    # image mt pioneer shock panama far     =_mt_pioneer_shock_panama['far'] 
    $ _mt_scared3_panama_pioneer = ComposeSpriteSet('normal', 'mt/mt_3_body.png',  'mt/mt_3_pioneer.png', 'mt/mt_3_scared3.png', 'mt/mt_3_panama.png')
    image mt scared3 panama pioneer  =_mt_scared3_panama_pioneer['normal']
    # $ _mt_pioneer_doubt = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_doubt.png')
    # image mt pioneer doubt close    =_mt_pioneer_doubt['close']
    # image mt pioneer doubt          =_mt_pioneer_doubt['normal']     
    # image mt pioneer doubt far      =_mt_pioneer_doubt['far'] 
    # $ _mt_pioneer_doubt_panama = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_doubt.png', 'images/3500/sprites/full/mt/mt_3_panama.png')
    # image mt pioneer doubt panama close   =_mt_pioneer_doubt_panama['close']
    # image mt pioneer doubt panama         =_mt_pioneer_doubt_panama['normal']     
    # image mt pioneer doubt panama far     =_mt_pioneer_doubt_panama['far'] 

    # cs 
    # $ _cs_fear = ComposeSprite('images/3500/sprites/full/cs/cs_1_body.png', 'scenario_uvao/images/cs_2_fear.png')
    # image cs fear close    = _cs_fear['close']
    # image cs fear          = _cs_fear['normal']
    # image cs fear far      = _cs_fear['far']
    # $ _cs_fear2 = ComposeSprite('scenario_uvao/images/cs_2_body.png', 'scenario_uvao/images/cs_2_fear.png')
    # image cs fear2 close    = _cs_fear2['close']
    # image cs fear2          = _cs_fear2['normal']
    # image cs fear2 far      = _cs_fear2['far']
    $ _cs_normal2 = ComposeSpriteSet('close', 'cs/cs_2_body.png', 'cs/cs_1_normal.png')
    image cs normal2 close    = _cs_normal2['close']
    # image cs normal2          = _cs_normal2['normal']
    # image cs normal2 far      = _cs_normal2['far']
    $ _cs_smile2 = ComposeSpriteSet( ('normal', 'close'), 'cs/cs_2_body.png',  'cs/cs_1_smile.png')
    image cs smile2 close    = _cs_smile2['close']
    image cs smile2          = _cs_smile2['normal']
    # image cs smile2 far      = _cs_smile2['far']
    # $ _cs_shy2 = ComposeSprite('scenario_uvao/images/cs_2_body.png', 'images/3500/sprites/full/cs/cs_1_shy.png')
    # image cs shy2 close    = _cs_shy2['close']
    # image cs shy2          = _cs_shy2['normal']
    # image cs shy2 far      = _cs_shy2['far']
    $ _cs_badgirl2 = ComposeSpriteSet('close', 'cs/cs_2_body.png', 'cs/cs_2_badgirl.png')
    image cs badgirl2 close    = _cs_badgirl2['close']
    # image cs badgirl2          = _cs_badgirl2['normal']
    # image cs badgirl2 far      = _cs_badgirl2['far']