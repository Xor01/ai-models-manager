from language_model import LanguageModel


class ModelManager:
    """"Class to manage multiple language models."""
    def __init__(self):
        self.models = [LanguageModel]

    def add_model(self, model: LanguageModel):
        self.models.append(model)

    def remove_model(self, model):
        self.models.remove(model)

    def get_model(self, model):
        try:
            return self.models[self.models.index(model)]
        except ValueError:
            return "This model does not exist."

    def list_models(self):
        for i, model in enumerate(self.models, start=1):
            print(f"{i}. Model: {model}")

    def select_model(self, provider, required_tokens):
        return map(lambda x:x.provider == provider and x.max_tokens >= required_tokens and x.__is_active(), self.models)
    

