#День4 Ходим по лагерю перед сном после второй встречи с Юлей
#
label uvao_D4_evening_business:
#День4 Ходим по лагерю перед сном после второй встречи с Юлей
#
    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset with fade
    play ambience ambience_camp_center_evening fadein 1
    window show
    "Снова вечер, снова недовольный Генда."
    "Я сел на скамейку напротив памятника и откинулся назад."
    th "Так, по крайней мере вырисовывается план действий."
    th "Завтра с самого утра отправляюсь в старый лагерь, к Юле в гости."
#    th "Надеюсь, от нее я узнаю больше, чем из учебников."
# Про что он узнает? про Генду?
    th "Надеюсь, не зря придётся ходить."



    stop ambience fadeout 5
    window hide

#    return
