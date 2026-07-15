from language_model import LanguageModel


class EmbeddingModel(LanguageModel):
    """Class to define the Embedding model."""
    def __init__(self, model_name, provider, max_tokens, temperature, model_type):
        super().__init__(model_name, provider, max_tokens, temperature, model_type)
    
    def generate_response(self, query):
        return [0.12, 0.45, 0.88, 0.31]
