from mycroft import MycroftSkill, intent_file_handler


class Checkpassword(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('checkpassword.intent')
    def handle_checkpassword(self, message):
        self.speak_dialog('checkpassword')


def create_skill():
    return Checkpassword()

