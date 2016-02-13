#Спрайты залить с гита в scenario_alt/pics/sprites
init 19:
#Диспозиция по CS следующая:
# без номера - ванильное тело с поднятой рукой
# 2 - рука горизонтально
# 3 - рука опущена вдоль тела
# important - рука поднята, указательный палец выпрямлен

    $ _cs_normal2_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_through.png')
    image cs normal2 glasses_thr close = _cs_normal2_glasses_thr['close']
    image cs normal2 glasses_thr = _cs_normal2_glasses_thr['normal']
    image cs normal2 glasses_thr far = _cs_normal2_glasses_thr['far']
    
    $ _cs_smile2_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_smile.png', 'cs/cs_1_glasses_through.png')
    image cs smile2 glasses_thr close = _cs_smile2_glasses_thr['close']
    image cs smile2 glasses_thr = _cs_smile2_glasses_thr['normal']
    image cs smile2 glasses_thr far = _cs_smile2_glasses_thr['far']
    
    $ _cs_smile2_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_smile.png', 'cs/cs_1_glasses_through.png')
    image cs smile2 glasses_thr close = _cs_smile2_glasses_thr['close']
    image cs smile2 glasses_thr = _cs_smile2_glasses_thr['normal']
    image cs smile2 glasses_thr far = _cs_smile2_glasses_thr['far']

    $ _cs_fear2_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_fear.png', 'cs/cs_1_glasses_through.png')
    image cs fear2 glasses_thr close = _cs_fear2_glasses_thr['close']
    image cs fear2 glasses_thr = _cs_fear2_glasses_thr['normal']
    image cs fear2 glasses_thr far = _cs_fear2_glasses_thr['far']
    
    $ _cs_laugh2_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_laugh.png', 'cs/cs_1_glasses_through.png')
    image cs laugh2 glasses_thr close = _cs_laugh2_glasses_thr['close']
    image cs laugh2 glasses_thr = _cs_laugh2_glasses_thr['normal']
    image cs laugh2 glasses_thr far = _cs_laugh2_glasses_thr['far']
    
    $ _cs_doubt2_glasses_thr = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_doubt.png', 'cs/cs_1_glasses_through.png')
    image cs doubt2 glasses_thr close = _cs_doubt2_glasses_thr['close']
    image cs doubt2 glasses_thr = _cs_doubt2_glasses_thr['normal']
    image cs doubt2 glasses_thr far = _cs_doubt2_glasses_thr['far']

    $ _cs_normal_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_1_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_over.png')
    image cs normal glasses_over close = _cs_normal_glasses_over['close']
    image cs normal glasses_over = _cs_normal_glasses_over['normal']
    image cs normal glasses_over far = _cs_normal_glasses_over['far']
    
    $ _cs_normal2_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_over.png')
    image cs normal2 glasses_over close = _cs_normal2_glasses_over['close']
    image cs normal2 glasses_over = _cs_normal2_glasses_over['normal']
    image cs normal2 glasses_over far = _cs_normal2_glasses_over['far']
    
    $ _cs_smile2_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_smile.png', 'cs/cs_1_glasses_over.png')
    image cs smile2 glasses_over close = _cs_smile2_glasses_over['close']
    image cs smile2 glasses_over = _cs_smile2_glasses_over['normal']
    image cs smile2 glasses_over far = _cs_smile2_glasses_over['far']
    
    $ _cs_laugh2_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_laugh.png', 'cs/cs_1_glasses_over.png')
    image cs laugh2 glasses_over close = _cs_laugh2_glasses_over['close']
    image cs laugh2 glasses_over = _cs_laugh2_glasses_over['normal']
    image cs laugh2 glasses_over far = _cs_laugh2_glasses_over['far']
    
    $ _cs_doubt2_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_doubt.png', 'cs/cs_1_glasses_over.png')
    image cs doubt2 glasses_over close = _cs_doubt2_glasses_over['close']
    image cs doubt2 glasses_over = _cs_doubt2_glasses_over['normal']
    image cs doubt2 glasses_over far = _cs_doubt2_glasses_over['far']

    $ _cs_badgirl3_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_2_badgirl.png', 'cs/cs_1_glasses_over.png')
    image cs badgirl3 glasses_over close = _cs_badgirl3_glasses_over['close']
    image cs badgirl3 glasses_over = _cs_badgirl3_glasses_over['normal']
    image cs badgirl3 glasses_over far = _cs_badgirl3_glasses_over['far']
    
    $ _cs_normal3_glasses_over = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses_over.png')
    image cs normal3 glasses_over close = _cs_normal3_glasses_over['close']
    image cs normal3 glasses_over = _cs_normal3_glasses_over['normal']
    image cs normal3 glasses_over far = _cs_normal3_glasses_over['far']
    
    $ _cs_laugh = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_1_body.png', 'cs/cs_2_laugh.png')
    image cs laugh close = _cs_laugh['close']
    image cs laugh = _cs_laugh['normal']
    image cs laugh far = _cs_laugh['far']
    
    $ _cs_laugh2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_laugh.png')
    image cs laugh2 close = _cs_laugh2['close']
    image cs laugh2 = _cs_laugh2['normal']
    image cs laugh2 far = _cs_laugh2['far']

    $ _cs_laugh3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_2_laugh.png')
    image cs laugh3 close = _cs_laugh3['close']
    image cs laugh3 = _cs_laugh3['normal']
    image cs laugh3 far = _cs_laugh3['far']

    image cs normal glasses = ComposeSpriteSet('normal', 'cs/cs_1_body.png', 'cs/cs_1_normal.png', 'cs/cs_1_glasses.png')['normal']
    
    $ _cs_fear2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_fear.png')
    image cs fear2 close = _cs_fear2['close']
    image cs fear2 = _cs_fear2['normal']
    image cs fear2 far = _cs_fear2['far']
    
    $ _cs_important = ComposeSpriteSet(('close', 'normal'), 'cs/cs_zhi.png', 'cs/cs_1_normal.png')
    image cs important close = _cs_important['close']
    image cs important = _cs_important['normal']
    
    $ _cs_smile3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_1_smile.png')
    image cs smile3 close = _cs_smile3['close']
    image cs smile3 = _cs_smile3['normal']
    image cs smile3 far = _cs_smile3['far']

    $ _cs_normal3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_1_normal.png')
    image cs normal3 close = _cs_normal3['close']
    image cs normal3 = _cs_normal3['normal']
    image cs normal3 far = _cs_normal3['far']

    $ _cs_badgirl2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_2_badgirl.png')
    image cs badgirl2 close = _cs_badgirl2['close']
    image cs badgirl2 = _cs_badgirl2['normal']
    image cs badgirl2 far = _cs_badgirl2['far']

    $ _cs_badgirl3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_2_badgirl.png')
    image cs badgirl3 close = _cs_badgirl3['close']
    image cs badgirl3 = _cs_badgirl3['normal']
    image cs badgirl3 far = _cs_badgirl3['far']

    $ _cs_shy2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_shy.png')
    image cs shy2 close = _cs_shy2['close']
    image cs shy2 = _cs_shy2['normal']
    image cs shy2 far = _cs_shy2['far']

    $ _cs_doubt2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_doubt.png')
#    $ _cs_doubt2 = ComposeSpriteSet(('close'), 'cs/cs_2_body.png', 'cs/cs_1_doubt.png')
    image cs doubt2 close = _cs_doubt2['close']
    image cs doubt2 = _cs_doubt2['normal']
    image cs doubt2 far = _cs_doubt2['far']

    $ _cs_doubt3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_1_doubt.png')
    image cs doubt3 close = _cs_doubt3['close']
    image cs doubt3 = _cs_doubt3['normal']
    image cs doubt3 far = _cs_doubt3['far']

    # CS sad
    $ _cs_sad1 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_1_body.png', 'cs/cs_sad.png')
    image cs sad close = _cs_sad1['close']
    image cs sad = _cs_sad1['normal']
    image cs sad far = _cs_sad1['far']

    $ _cs_sad2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_sad.png')
    image cs sad2 close = _cs_sad2['close']
    image cs sad2 = _cs_sad2['normal']
    image cs sad2 far = _cs_sad2['far']

    $ _cs_sad3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_sad.png')
    image cs sad3 close = _cs_sad3['close']
    image cs sad3 = _cs_sad3['normal']
    image cs sad3 far = _cs_sad3['far']

    # CS stressed
    $ _cs_stressed1 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_1_body.png', 'cs/cs_stressed.png')
    image cs stressed close = _cs_stressed1['close']
    image cs stressed = _cs_stressed1['normal']
    image cs stressed far = _cs_stressed1['far']

    $ _cs_stressed2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_stressed.png')
    image cs stressed2 close = _cs_stressed2['close']
    image cs stressed2 = _cs_stressed2['normal']
    image cs stressed2 far = _cs_stressed2['far']

    $ _cs_stressed3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_stressed.png')
    image cs stressed3 close = _cs_stressed3['close']
    image cs stressed3 = _cs_stressed3['normal']
    image cs stressed3 far = _cs_stressed3['far']

    # CS upset
    $ _cs_upset1 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_1_body.png', 'cs/cs_upset.png')
    image cs upset close = _cs_upset1['close']
    image cs upset = _cs_upset1['normal']
    image cs upset far = _cs_upset1['far']

    $ _cs_upset2 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_2_body.png', 'cs/cs_upset.png')
    image cs upset2 close = _cs_upset2['close']
    image cs upset2 = _cs_upset2['normal']
    image cs upset2 far = _cs_upset2['far']

    $ _cs_upset3 = ComposeSpriteSet(('close', 'normal', 'far'), 'cs/cs_3_body.png', 'cs/cs_upset.png')
    image cs upset3 close = _cs_upset3['close']
    image cs upset3 = _cs_upset3['normal']
    image cs upset3 far = _cs_upset3['far']


    # Унылка
    image un cry wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_cry.png')['normal']
    image un cry_smile wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_cry_smile.png')['normal']
    image un sad wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_sad.png')['normal']
    image un scared wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_scared.png')['normal']
    image un shocked wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_shocked.png')['normal']
    image un surprise wet_dress = ComposeSpriteSet('normal', 'un/un_2_wet_body.png', 'un/un_2_surprise.png')['normal']

    # image un sorrow pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), get_sprite_ori('normal/un/un_1_body.png'), (0, 0), get_sprite_ori('normal/un/un_1_pioneer.png'), (0, 0), get_sprite_7dl('normal/un/un_1_sorrow.png')), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080),  (0, 0), get_sprite_ori('normal/un/un_1_body.png'), (0, 0), get_sprite_ori('normal/un/un_1_pioneer.png'), (0, 0), get_sprite_7dl('normal/un/un_1_sorrow.png')), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1050, 1080),  (0, 0), get_sprite_ori('normal/un/un_1_body.png'), (0, 0), get_sprite_ori('normal/un/un_1_pioneer.png'), (0, 0), get_sprite_7dl('normal/un/un_1_sorrow.png')))

    # $ _un_sorrow_pioneer = ComposeSpriteSet(('close', 'normal', 'far'), 'un/un_1_body.png', 'un/un_1_pioneer.png', 'un/un_1_sorrow.png')
    # image un sorrow pioneer close = _un_sorrow_pioneer['close']
    # image un sorrow pioneer = _un_sorrow_pioneer['normal']
    # image un sorrow pioneer far = _un_sorrow_pioneer['far']
    
    # Юля неглиже
    # image uv smile naked close = ComposeSpriteSet('close', 'uv/uv_2_body_naked.png', '###uv_smile###')['close'] - нужен PNG эмоции
    # image uv normal close
    # image uv guilty naked close
    # image uv surprise naked close
    # image uv laugh close 
    
    #25ти-летняя Славя
    $ _sl_25_normal = ComposeSpriteSet(('normal', 'far'), 'sl/sl_25_body.png', 'sl/sl_25_neutral.png')
    image sl 25 normal = _sl_25_normal['normal']
    image sl 25 normal far = _sl_25_normal['far']
    
    $ _sl_25_fear_1 = ComposeSpriteSet(('normal', 'far'), 'sl/sl_25_body.png', 'sl/sl_25_fear_1.png')
    image sl 25 fear_1 = _sl_25_fear_1['normal']
    image sl 25 fear_1 far = _sl_25_fear_1['far']
    
    $ _sl_25_fear_2 = ComposeSpriteSet(('normal', 'far'), 'sl/sl_25_body.png', 'sl/sl_25_fear_2.png')
    image sl 25 fear_2 = _sl_25_fear_2['normal']
    image sl 25 fear_2 far = _sl_25_fear_2['far']
    
    $ _sl_25_displeased = ComposeSpriteSet(('normal', 'far'), 'sl/sl_25_body.png', 'sl/sl_25_displeased.png')
    image sl 25 displeased = _sl_25_displeased['normal']
    image sl 25 displeased far = _sl_25_displeased['far']

    # feared ОД в панаме (close и far спрайтов нет)
    image mt feared panama pioneer = ComposeSpriteSet('normal', 'mt/mt_3_body.png', 'mt/mt_3_pioneer.png', 'mt/mt_3_feared.png', 'mt/mt_3_panama.png')['normal']

    