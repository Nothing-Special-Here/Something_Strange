init 18:
#    image el slap pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/1080/sprites_new/normal/el/el_2_body.png', (0, 0), 'images/1080/sprites_new/normal/el/el_2_pioneer.png', (0, 0), 'scenario_uvao/images/el_slap.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080),  (0, 0), 'images/1080/sprites_new/normal/el/el_2_body.png', (0, 0), 'images/1080/sprites_new/normal/el/el_2_pioneer.png', (0, 0), 'scenario_uvao/images/el_slap.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1050, 1080),  (0, 0), 'images/1080/sprites_new/normal/el/el_2_body.png', (0, 0), 'images/1080/sprites_new/normal/el/el_2_pioneer.png', (0, 0), 'scenario_uvao/images/el_slap.png'))
        
    # запчасти 3500х1500
    $ _el_2_body    = im.Image('images/3500/sprites/full/el/el_2_body.png')
    $ _el_2_pioneer = im.Image('images/3500/sprites/full/el/el_2_pioneer.png')
    $ _el_2_fingal  = im.Image('images/3500/sprites/full/el/el_2_fingal.png')
    $ _el_2_slap    = im.Image('scenario_uvao/images/el_slap.png')
    
    $ _sh_angry_bar = im.Image('scenario_uvao/images/sh_angry_bar.png')
    
    # сборка 3500x1500
    $ _el_2_body_pioneer_fingal = im.Composite(None, (0,0), _el_2_body, (0,0), _el_2_pioneer, (0,0), _el_2_fingal)
    $ _el_2_body_pioneer_slap   = im.Composite(None, (0,0), _el_2_body, (0,0), _el_2_pioneer, (0,0), _el_2_slap)
   
    
    # resize под close (1125), normal(900), far(675)
    $ _el_2_body_pioneer_fingal_close   = im.Crop(im.Scale(_el_2_body_pioneer_fingal, 1125, 2625), 0, 0, 1125, 1080)
    $ _el_2_body_pioneer_slap_close     = im.Crop(im.Scale(_el_2_body_pioneer_slap, 1125, 2625), 0, 0, 1125, 1080)
    $ _el_2_body_pioneer_fingal_normal  = im.Crop(im.Scale(_el_2_body_pioneer_fingal, 900, 2100), 0, 0, 900, 1080)
    $ _el_2_body_pioneer_slap_normal    = im.Crop(im.Scale(_el_2_body_pioneer_slap, 900, 2100), 0, 0, 900, 1080)    
    $ _el_2_body_pioneer_fingal_far     = im.Crop(im.Scale(_el_2_body_pioneer_fingal, 675, 1575), 0, 0, 675, 1080) 
    $ _el_2_body_pioneer_slap_far       = im.Crop(im.Scale(_el_2_body_pioneer_slap, 675, 1575), 0, 0, 675, 1080) 
    
    $ _sh_angry_bar_close               = im.Crop(im.Scale(_sh_angry_bar, 1125, 2625), 0, 0, 1125, 1080)
    $ _sh_angry_bar_normal              = im.Crop(im.Scale(_sh_angry_bar, 900, 2100), 0, 0, 900, 1080)
    $ _sh_angry_bar_far                 = im.Crop(im.Scale(_sh_angry_bar, 675, 1575), 0, 0, 675, 1080)
    
    # сами спрайты, с тонировкой под закат или ночь
    image el pioneer slap close = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_el_2_body_pioneer_slap_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_el_2_body_pioneer_slap_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _el_2_body_pioneer_slap_close)
    image el pioneer slap       = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_el_2_body_pioneer_slap_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_el_2_body_pioneer_slap_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _el_2_body_pioneer_slap_normal)
    image el pioneer slap far   = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_el_2_body_pioneer_slap_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_el_2_body_pioneer_slap_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _el_2_body_pioneer_slap_far)
                                                    
    image sh angry bar close    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar_close)
    image sh angry bar          = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar_normal)
    image sh angry bar far      = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar_far)