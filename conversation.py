from language_model import LanguageModel


class Conversation:
    """Class to define the conversation between the user and the AI model."""

    def __init__(self, conversation_id, model: LanguageModel):
        self.conversation_id = conversation_id
        self.model = model
        self.messages = []

    def send_message(self, message: str):
        self.messages.append({'role': 'user', 'content': message})
        response = self.model.generate_response(message)
        self.messages.append({'role': 'ai response', 'content': response})

    def display_history(self):
        for conversation in self.messages:
            print(f"[{conversation['role']}] {conversation['content']}")
