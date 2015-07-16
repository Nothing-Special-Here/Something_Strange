#Спрайты залить с гита в scenario_alt/pics/sprites
init 19:
    $ _cs_normal_glasses_thru = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_through.png')
    image cs normal glasses_thru close = _cs_normal_glasses_thru['close']
    image cs normal glasses_thru = _cs_normal_glasses_thru['normal']
    
    $ _cs_fear_glasses_thru = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_fear.png', 'cs/cs_1_glasses_through.png')
    image cs fear glasses_thru close = _cs_fear_glasses_thru['close']
    image cs fear glasses_thru = _cs_fear_glasses_thru['normal']
    
    image cs normal glasses = ComposeSpriteSet(('normal', 'far'), 'cs/cs_1_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses.png')['normal']
    
    $ _cs_fear = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_fear.png')
    image cs fear close = _cs_fear['close']
    image cs fear = _cs_fear['normal']
    image cs fear far = _cs_fear['far']
    
    image un cry wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_cry.png')['normal']
    image un cry_smile wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_cry_smile.png')['normal']
    image un sad wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_sad.png')['normal']
    image un scared wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_scared.png')['normal']
    image un shocked wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_shocked.png')['normal']
    image un surprise wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_surprise.png')['normal']