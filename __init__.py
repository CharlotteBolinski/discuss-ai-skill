from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class DiscussAi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('WhatIsAi').require('What')
                    .require('Ai'))
    def handle_what_is(self, message):
        self.speak_dialog('ai.description')

   @intent_handler(IntentBuilder('TellMeMore')
                    .require('More').require('Ai').one_of('Know', 'Tell').one_of('You', 'I'))
    def handle_tell_me_more(self, message):
        self.speak_dialog('question.ai.generic')

    @intent_handler(IntentBuilder('MakeSuggestion').require('Suggestion')
                    .optionally('Topic').optionally('I','My'))
    def handle_do_you_like(self, message):
        ai_topic = message.data.get('Topic')
        if ai_topic is not None:
            self.speak_dialog('topic.ai',
                              {'type': ai_topic})
        else:
            self.speak_dialog('did.not.get.generic')

def create_skill():
    return DiscussAi()

