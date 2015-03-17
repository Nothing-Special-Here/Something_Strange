init 18:
# коэффициенты
    $ _factor_close = 0.75
    $ _factor_normal = 0.6
    $ _factor_far = 0.45
# запчасти 3500х1500
    # el
    $ _el_2_body    = im.Image('images/3500/sprites/full/el/el_2_body.png')
    $ _el_2_pioneer = im.Image('images/3500/sprites/full/el/el_2_pioneer.png')
    $ _el_2_slap    = im.Image('scenario_uvao/images/el_slap.png')
    # mt
    $ _mt_3_body    = im.Image('images/3500/sprites/full/mt/mt_3_body.png')
    $ _mt_3_pioneer = im.Image('images/3500/sprites/full/mt/mt_3_pioneer.png')
    $ _mt_3_doubt   = im.Image('scenario_uvao/images/mt_doubt.png')
    $ _mt_3_shock  = im.Image('scenario_uvao/images/mt_shock.png')
    $ _mt_3_panama  = im.Image('images/3500/sprites/full/mt/mt_3_panama.png')
    # sh
    $ _sh_angry_bar = im.Image('scenario_uvao/images/sh_angry_bar.png')
    $ _sh_angry_bar2 = im.Image('scenario_uvao/images/sh_angry_bar2.png')
    $ _sh_angry_bar3 = im.Image('scenario_uvao/images/sh_angry_bar3.png')
    # cs
    $ _cs_1_body = im.Image('images/3500/sprites/full/cs/cs_1_body.png')
    $ _cs_2_body = im.Image('scenario_uvao/images/cs_2_body.png')
    $ _cs_3_body = im.Image('scenario_uvao/images/cs_zhi.png')
    $ _cs_normal = im.Image('images/3500/sprites/full/cs/cs_normal.png')
    $ _cs_shy = im.Image('images/3500/sprites/full/cs/cs_shy.png')
    $ _cs_smile = im.Image('scenario_uvao/images/cs_smile.png')
    $ _cs_fear = im.Image('scenario_uvao/images/cs_2_fear.png')  
    
# сборка 3500x1500
    # el
    $ _el_2_pioneer_slap   = im.Composite(None, (0,0), _el_2_body, (0,0), _el_2_pioneer, (0,0), _el_2_slap)
    #mt
    $ _mt_3_pioneer_doubt  = im.Composite(None, (0,0), _mt_3_body, (0,0), _mt_3_pioneer, (0,0), _mt_3_doubt)
    $ _mt_3_pioneer_doubt_panama  = im.Composite(None, (0,0), _mt_3_body, (0,0), _mt_3_pioneer, (0,0), _mt_3_doubt, (0,0), _mt_3_panama)
    $ _mt_3_pioneer_shock  = im.Composite(None, (0,0), _mt_3_body, (0,0), _mt_3_pioneer, (0,0), _mt_3_shock)
    $ _mt_3_pioneer_shock_panama  = im.Composite(None, (0,0), _mt_3_body, (0,0), _mt_3_pioneer, (0,0), _mt_3_shock, (0,0), _mt_3_panama)
    #cs
    $ _cs_1 = im.Composite(None, (0,0), _cs_1_body, (0,0), _cs_normal)
    $ _cs_1_shy = im.Composite(None, (0,0), _cs_1_body, (0,0), _cs_shy)
    $ _cs_1_smile = im.Composite(None, (0,0), _cs_1_body, (0,0), _cs_smile)    
    $ _cs_1_fear = im.Composite(None, (0,0), _cs_1_body, (0,0), _cs_fear)    
    $ _cs_2 = im.Composite(None, (0,0), _cs_2_body, (0,0), _cs_normal)
    $ _cs_2_shy = im.Composite(None, (0,0), _cs_2_body, (0,0), _cs_shy)
    $ _cs_2_smile = im.Composite(None, (0,0), _cs_2_body, (0,0), _cs_smile)    
    $ _cs_2_fear = im.Composite(None, (0,0), _cs_2_body, (0,0), _cs_fear)    
  
    
    # resize под close (1125), normal(900), far(675)
    # el
    $ _el_2_body_pioneer_slap_close     = im.Crop(im.FactorScale(_el_2_pioneer_slap, _factor_close), 0, 0, 1125, 1080)
    $ _el_2_body_pioneer_slap_normal    = im.Crop(im.FactorScale(_el_2_pioneer_slap, _factor_normal), 0, 0, 900, 1080)    
    $ _el_2_body_pioneer_slap_far       = im.Crop(im.FactorScale(_el_2_pioneer_slap, _factor_far), 0, 0, 675, 1080) 
    # sh
    $ _sh_angry_bar_close               = im.Crop(im.FactorScale(_sh_angry_bar, _factor_close), 0, 0, 1125, 1080)
    $ _sh_angry_bar_normal              = im.Crop(im.FactorScale(_sh_angry_bar, _factor_normal), 0, 0, 900, 1080)
    $ _sh_angry_bar_far                 = im.Crop(im.FactorScale(_sh_angry_bar, _factor_far), 0, 0, 675, 1080)
    $ _sh_angry_bar2_close               = im.Crop(im.FactorScale(_sh_angry_bar2, _factor_close), 0, 0, 1125, 1080)
    $ _sh_angry_bar2_normal              = im.Crop(im.FactorScale(_sh_angry_bar2, _factor_normal), 0, 0, 900, 1080)
    $ _sh_angry_bar2_far                 = im.Crop(im.FactorScale(_sh_angry_bar2, _factor_far), 0, 0, 675, 1080)
    $ _sh_angry_bar3_close               = im.Crop(im.FactorScale(_sh_angry_bar3, _factor_close), 0, 0, 1125, 1080)
    $ _sh_angry_bar3_normal              = im.Crop(im.FactorScale(_sh_angry_bar3, _factor_normal), 0, 0, 900, 1080)
    $ _sh_angry_bar3_far                 = im.Crop(im.FactorScale(_sh_angry_bar3, _factor_far), 0, 0, 675, 1080)
    # mt
    $ _mt_3_pioneer_doubt_close         = im.Crop(im.FactorScale(_mt_3_pioneer_doubt, _factor_close), 0, 0, 1125, 1080)
    $ _mt_3_pioneer_doubt_normal        = im.Crop(im.FactorScale(_mt_3_pioneer_doubt, _factor_normal), 0, 0, 900, 1080)
    $ _mt_3_pioneer_doubt_far           = im.Crop(im.FactorScale(_mt_3_pioneer_doubt, _factor_far), 0, 0, 675, 1080)
    $ _mt_3_pioneer_doubt_panama_close  = im.Crop(im.FactorScale(_mt_3_pioneer_doubt_panama, _factor_close), 0, 0, 1125, 1080)
    $ _mt_3_pioneer_doubt_panama_normal = im.Crop(im.FactorScale(_mt_3_pioneer_doubt_panama, 900, 2100), 0, 0, 900, 1080)
    $ _mt_3_pioneer_doubt_panama_far    = im.Crop(im.FactorScale(_mt_3_pioneer_doubt_panama, 675, 1575), 0, 0, 675, 1080)
    $ _mt_3_pioneer_shock_close        = im.Crop(im.FactorScale(_mt_3_pioneer_shock, _factor_close), 0, 0, 1125, 1080)
    $ _mt_3_pioneer_shock_normal       = im.Crop(im.FactorScale(_mt_3_pioneer_shock, _factor_normal), 0, 0, 900, 1080)
    $ _mt_3_pioneer_shock_far          = im.Crop(im.FactorScale(_mt_3_pioneer_shock, _factor_far), 0, 0, 675, 1080)
    $ _mt_3_pioneer_shock_panama_close = im.Crop(im.FactorScale(_mt_3_pioneer_shock_panama, _factor_close), 0, 0, 1125, 1080)
    $ _mt_3_pioneer_shock_panama_normal= im.Crop(im.FactorScale(_mt_3_pioneer_shock_panama, _factor_normal), 0, 0, 900, 1080)
    $ _mt_3_pioneer_shock_panama_far   = im.Crop(im.FactorScale(_mt_3_pioneer_shock_panama, _factor_far), 0, 0, 675, 1080)
    #cs
    $ _cs_1_fear_close                  = im.Crop(im.FactorScale(_cs_1_fear, _factor_close), 0, 0, 1125, 1080)
    $ _cs_1_fear_normal                 = im.Crop(im.FactorScale(_cs_1_fear, _factor_normal), 0, 0, 900, 1080)
    $ _cs_1_fear_far                    = im.Crop(im.FactorScale(_cs_1_fear, _factor_far), 0, 0, 675, 1080)
    $ _cs_2_fear_close                  = im.Crop(im.FactorScale(_cs_2_fear, _factor_close), 0, 0, 1125, 1080)
    $ _cs_2_fear_normal                 = im.Crop(im.FactorScale(_cs_2_fear, _factor_normal), 0, 0, 900, 1080)
    $ _cs_2_fear_far                    = im.Crop(im.FactorScale(_cs_2_fear, _factor_far), 0, 0, 675, 1080)

    
#####################################################    
# сами спрайты, с тонировкой под закат или ночь
#####################################################
    # el
    image el pioneer slap close = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_el_2_body_pioneer_slap_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_el_2_body_pioneer_slap_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _el_2_body_pioneer_slap_close)
    image el pioneer slap       = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_el_2_body_pioneer_slap_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_el_2_body_pioneer_slap_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _el_2_body_pioneer_slap_normal)
    image el pioneer slap far   = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_el_2_body_pioneer_slap_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_el_2_body_pioneer_slap_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _el_2_body_pioneer_slap_far)
                                                    
    #sh                                                
    image sh angry bar close    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar_close)
    image sh angry bar          = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar_normal)
    image sh angry bar far      = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar_far)
    image sh angry bar2 close    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar2_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar2_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar2_close)
    image sh angry bar2          = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar2_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar2_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar2_normal)
    image sh angry bar2 far      = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar2_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar2_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar2_far)    
    image sh angry bar3 close    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar3_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar3_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar3_close)
    image sh angry bar3          = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar3_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar3_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar3_normal)
    image sh angry bar3 far      = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_sh_angry_bar3_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_sh_angry_bar3_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _sh_angry_bar3_far)    
                                                    
    #mt
    image mt pioneer shock close=ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_shock_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_shock_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_shock_close) 
    image mt pioneer shock     = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_shock_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_shock_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_shock_normal)     
    image mt pioneer shock far = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_shock_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_shock_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_shock_far)                                                     
    image mt pioneer shock panama close=ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_shock_panama_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_shock_panama_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_shock_panama_close) 
    image mt pioneer shock panama    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_shock_panama_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_shock_panama_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_shock_panama_normal)     
    image mt pioneer shock panama far = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_shock_panama_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_shock_panama_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_shock_panama_far)  
    image mt pioneer doubt close=ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_doubt_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_doubt_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_doubt_close) 
    image mt pioneer doubt     = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_doubt_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_doubt_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_doubt_normal)     
    image mt pioneer doubt far = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_doubt_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_doubt_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_doubt_far)                                                     
    image mt pioneer doubt panama close=ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_doubt_panama_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_doubt_panama_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_doubt_panama_close) 
    image mt pioneer doubt panama    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_doubt_panama_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_doubt_panama_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_doubt_panama_normal)     
    image mt pioneer doubt panama far = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_mt_3_pioneer_doubt_panama_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_mt_3_pioneer_doubt_panama_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _mt_3_pioneer_doubt_panama_far)                                                        
    #cs                                                
    image cs fear close    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_cs_1_fear_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_cs_1_fear_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _cs_1_fear_close)
    image cs fear          = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_cs_1_fear_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_cs_1_fear_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _cs_1_fear_normal)
    image cs far      = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_cs_1_fear_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_cs_1_fear_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _cs_1_fear_far)
    image cs fear2 close    = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_cs_2_fear_close, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_cs_2_fear_close, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _cs_2_fear_close)
    image cs fear2          = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_cs_2_fear_normal, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_cs_2_fear_normal, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _cs_2_fear_normal)
    image cs fear2 far      = ConditionSwitch(  "persistent.sprite_time=='sunset'", im.MatrixColor(_cs_2_fear_far, im.matrix.tint(0.94, 0.82, 1.0)), 
                                                    "persistent.sprite_time=='night'", im.MatrixColor(_cs_2_fear_far, im.matrix.tint(0.63, 0.78, 0.82)), 
                                                    True, _cs_2_fear_far)    
 
