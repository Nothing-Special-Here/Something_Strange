init:
    $ filters["widget__audio"] = u"Текущие звуки"

python early:
    def widget__audio():
        import os
        def editoverlay():
            line_ypos = 40
            audio_music = renpy.music.get_playing(channel='music')
            ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=line_ypos, xpadding=6, xminimum=200)
            ui.text("music: %s" % (audio_music), style="button_text", size=14)
            audio_ambience = renpy.music.get_playing(channel='ambience')
            ui.button(clicked=None, xpos=0.75, xanchor=1.0, ypos=line_ypos, xpadding=6, xminimum=200)
            ui.text("ambience: %s" % (audio_ambience), style="button_text", size=14)
            audio_sound_loop = renpy.music.get_playing(channel='sound_loop')
            ui.button(clicked=None, xpos=0.5, xanchor=1.0, ypos=line_ypos, xpadding=6, xminimum=200)
            ui.text("sound_loop: %s" % (audio_sound_loop), style="button_text", size=14)
            audio_sound = renpy.music.get_playing(channel='sound')
            ui.button(clicked=None, xpos=0.25, xanchor=1.0, ypos=line_ypos, xpadding=6, xminimum=200)
            ui.text("sound: %s" % (audio_sound), style="button_text", size=14)
        config.overlay_functions.append(editoverlay)
