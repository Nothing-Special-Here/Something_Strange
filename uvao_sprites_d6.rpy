#Спрайты залить с гита в scenario_alt/pics/sprites
init 19:
    $ _cs_normal_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_through.png')
    image cs normal glasses_thr close = _cs_normal_glasses_thr['close']
    image cs normal glasses_thr = _cs_normal_glasses_thr['normal']
    image cs normal glasses_thr far = _cs_normal_glasses_thr['far']
    
    $ _cs_smile_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_smile.png', 'cs/cs_1_glasses_through.png')
    image cs smile glasses_thr close = _cs_smile_glasses_thr['close']
    image cs smile glasses_thr = _cs_smile_glasses_thr['normal']
    image cs smile glasses_thr far = _cs_smile_glasses_thr['far']
    
    $ _cs_smile_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_smile.png', 'cs/cs_1_glasses_through.png')
    image cs smile glasses_thr close = _cs_smile_glasses_thr['close']
    image cs smile glasses_thr = _cs_smile_glasses_thr['normal']
    image cs smile glasses_thr far = _cs_smile_glasses_thr['far']

    $ _cs_fear_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_fear.png', 'cs/cs_1_glasses_through.png')
    image cs fear glasses_thr close = _cs_fear_glasses_thr['close']
    image cs fear glasses_thr = _cs_fear_glasses_thr['normal']
    image cs fear glasses_thr far = _cs_fear_glasses_thr['far']
    
    $ _cs_normal_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_over.png')
    image cs normal glasses_over close = _cs_normal_glasses_over['close']
    image cs normal glasses_over = _cs_normal_glasses_over['normal']
    image cs normal glasses_over far = _cs_normal_glasses_over['far']
    
    $ _cs_smile_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_smile.png', 'cs/cs_1_glasses_over.png')
    image cs smile glasses_over close = _cs_smile_glasses_over['close']
    image cs smile glasses_over = _cs_smile_glasses_over['normal']
    image cs smile glasses_over far = _cs_smile_glasses_over['far']
    
    image cs normal glasses = ComposeSpriteSet('normal', 'cs/cs_1_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses.png')['normal']

    
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