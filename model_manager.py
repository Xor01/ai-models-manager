from model_type import ModelType


class ModelManager:

    def __init__(self, model_type: ModelType):
        self.models = []
        self.model_type = model_type

    def add_model(self, model):
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
    

