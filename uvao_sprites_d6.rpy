#Спрайты залить с гита в scenario_alt/pics/sprites
init 19:
    $ _cs_normal_glasses_thru = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_normal.png', 'cs/cs_1_glasses_through.png')
    image cs normal glasses_thru close = _cs_normal_glasses_thru['close']
    image cs normal glasses_thru = _cs_normal_glasses_thru['normal']
    image cs normal glasses_thru far = _cs_normal_glasses_thru['far']
    
    $ _cs_normal_glasses = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_normal.png', 'cs/cs_1_glasses.png')
    image cs normal glasses close = _cs_normal_glasses_on['close']
    image cs normal glasses = _cs_normal_glasses_on['normal']
    image cs normal glasses far = _cs_normal_glasses_on['far']