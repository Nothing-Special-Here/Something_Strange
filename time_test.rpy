init:
    $ mods["time_test"] = u"Time Test"
    $ config.developer = True

init python:
    from time import localtime, strftime
    hour = strftime("%H", localtime())

label time_test:
    if hour in [23, 24, 0, 1, 2, 3, 4]:
        scene bg ext_road_night with dissolve
        "Ночь."
    elif hour in [20, 21, 22] or hour in [5, 6, 7, 8, 9]:
        scene bg ext_road_sunset with dissolve
        "Утро или Вечер."
    else:
        scene bg ext_road_day with dissolve
        "День."
     
    jump time_test