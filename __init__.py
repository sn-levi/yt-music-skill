from mycroft import MycroftSkill, intent_handler


class YtMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('music.yt.intent')
    def handle_music_yt(self, message):
        self.speak_dialog('music.yt')


def create_skill():
    return YtMusic()

