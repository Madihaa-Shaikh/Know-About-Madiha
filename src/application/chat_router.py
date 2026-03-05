from src.domain.chat_model import ChatModel

class ChatRouter:

    def __init__(self, info_model, general_model):
        self.info_model = info_model
        self.general_model = general_model

    def reply(self, message, mode):

        if mode == "I am Madiha (talk to me)":
            return self.info_model.reply(message)

        return self.general_model.reply(message)