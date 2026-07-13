from InvalidPromptError import InvalidPromptError
from language_model import LanguageModel


class LlamaModel(LanguageModel):
    def __init__(self, model_name: str, provider: str, max_tokens: int, temperature: float, model_path: str, quantization: str):
        super().__init__(model_name, provider, max_tokens, temperature)
        self.model_path = model_path
        self.quantization = quantization

    def generate_response(self, query):
        if not self.isPromptValid(query):
            raise InvalidPromptError
        return f'Local Llama API response to: {query}\nInput Tokens: {self.tokenizer.count_tokens(query)}'