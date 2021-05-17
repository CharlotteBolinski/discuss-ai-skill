from mycroft import MycroftSkill, intent_file_handler


class DiscussAi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ai.discuss.intent')
    def handle_ai_discuss(self, message):
        self.speak_dialog('ai.discuss')


def create_skill():
    return DiscussAi()

