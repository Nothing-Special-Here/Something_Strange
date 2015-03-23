init python:
    # Функция, собирающая спрайты из запчастей
    # argv - файлы-запчасти под 3500
    # на выходе - 9 спрайтов: far, close normal тонированные под day, night, sunset
    def ComposeSprite( *argv):
        # Множитель для разных размеров
        factor_close = 0.75
        factor_normal = 0.6
        factor_far = 0.45
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
        # ресайз и кроп под far, normal, close
        sprite_close =  im.Crop(im.FactorScale(large_sprite, factor_close),  0, 0, 1125, 1080)
        sprite_norm =   im.Crop(im.FactorScale(large_sprite, factor_normal), 0, 0, 900, 1080)
        sprite_far =    im.Crop(im.FactorScale(large_sprite, factor_far),    0, 0, 675, 1080)
        # дополнительно тонируем и возвращаем 9 штук
        return {'far day': sprite_far, 
                'normal day': sprite_norm, 
                'close day': sprite_close,
                'far night':im.MatrixColor(sprite_far, tint_night),
                'normal night': im.MatrixColor(sprite_norm, tint_night),
                'close night': im.MatrixColor(sprite_close, tint_night),
                'far sunset':im.MatrixColor(sprite_far, tint_sunset),
                'normal sunset': im.MatrixColor(sprite_norm, tint_sunset),
                'close sunset': im.MatrixColor(sprite_close, tint_sunset)   }            
init:

#####################################################    
# спрайты, с тонировкой под закат или ночь
#####################################################
    # el
    $ _el_pioneer_slap = ComposeSprite('images/3500/sprites/full/el/el_2_body.png', 'images/3500/sprites/full/el/el_2_pioneer.png','scenario_uvao/images/el_slap.png')
    image el pioneer slap close = _el_pioneer_slap['close ' + persistent.sprite_time]
    image el pioneer slap       = _el_pioneer_slap['normal ' + persistent.sprite_time]
    image el pioneer slap far   = _el_pioneer_slap['far ' + persistent.sprite_time]
                                                    
    #sh
    $ _sh_angry_bar = ComposeSprite('scenario_uvao/images/sh_angry_bar.png')
    image sh angry bar close    = _sh_angry_bar['close ' + persistent.sprite_time]
    image sh angry bar          = _sh_angry_bar['normal ' + persistent.sprite_time]
    image sh angry bar far      = _sh_angry_bar['far ' + persistent.sprite_time]
    $ _sh_angry_bar2 = ComposeSprite('scenario_uvao/images/sh_angry_bar2.png')
    image sh angry bar2 close    = _sh_angry_bar2['close ' + persistent.sprite_time]
    image sh angry bar2          = _sh_angry_bar2['normal ' + persistent.sprite_time]
    image sh angry bar2 far      = _sh_angry_bar2['far ' + persistent.sprite_time]   
    $ _sh_angry_bar3 = ComposeSprite('scenario_uvao/images/sh_angry_bar3.png')
    image sh angry bar3 close    = _sh_angry_bar3['close ' + persistent.sprite_time]
    image sh angry bar3          = _sh_angry_bar3['normal ' + persistent.sprite_time]
    image sh angry bar3 far      = _sh_angry_bar3['far ' + persistent.sprite_time]
                                                    
    #mt
    $ _mt_pioneer_shock = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_shock.png')
    image mt pioneer shock close    =_mt_pioneer_shock['close ' + persistent.sprite_time]
    image mt pioneer shock          =_mt_pioneer_shock['normal ' + persistent.sprite_time]     
    image mt pioneer shock far      =_mt_pioneer_shock['far ' + persistent.sprite_time] 
    $ _mt_pioneer_shock_panama = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_shock.png', 'images/3500/sprites/full/mt/mt_3_panama.png')
    image mt pioneer shock panama close   =_mt_pioneer_shock_panama['close ' + persistent.sprite_time]
    image mt pioneer shock panama         =_mt_pioneer_shock_panama['normal ' + persistent.sprite_time]     
    image mt pioneer shock panama far     =_mt_pioneer_shock_panama['far ' + persistent.sprite_time] 
    $ _mt_pioneer_doubt = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_doubt.png')
    image mt pioneer doubt close    =_mt_pioneer_doubt['close ' + persistent.sprite_time]
    image mt pioneer doubt          =_mt_pioneer_doubt['normal ' + persistent.sprite_time]     
    image mt pioneer doubt far      =_mt_pioneer_doubt['far ' + persistent.sprite_time] 
    $ _mt_pioneer_doubt_panama = ComposeSprite('images/3500/sprites/full/mt/mt_3_body.png', 'images/3500/sprites/full/mt/mt_3_pioneer.png', 'scenario_uvao/images/mt_doubt.png', 'images/3500/sprites/full/mt/mt_3_panama.png')
    image mt pioneer doubt panama close   =_mt_pioneer_doubt_panama['close ' + persistent.sprite_time]
    image mt pioneer doubt panama         =_mt_pioneer_doubt_panama['normal ' + persistent.sprite_time]     
    image mt pioneer doubt panama far     =_mt_pioneer_doubt_panama['far ' + persistent.sprite_time] 
                                                      
    #cs 
    $ _cs_fear = ComposeSprite('images/3500/sprites/full/cs/cs_1_body.png', 'scenario_uvao/images/cs_2_fear.png')
    image cs fear close    = _cs_fear['close ' + persistent.sprite_time]
    image cs fear          = _cs_fear['normal ' + persistent.sprite_time]
    image cs fear far      = _cs_fear['far ' + persistent.sprite_time]
    $ _cs_fear2 = ComposeSprite('scenario_uvao/images/cs_2_body.png', 'scenario_uvao/images/cs_2_fear.png')
    image cs fear2 close    = _cs_fear2['close ' + persistent.sprite_time]
    image cs fear2          = _cs_fear2['normal ' + persistent.sprite_time]
    image cs fear2 far      = _cs_fear2['far ' + persistent.sprite_time]
 
