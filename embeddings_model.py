from language_model import LanguageModel


class EmbeddingModel(LanguageModel):
    def __init__(self, model_name, provider, max_tokens, temperature):
        super().__init__(model_name, provider, max_tokens, temperature)
    
    def generate_response(query):
        return [0.12, 0.45, 0.88, 0.31]
