from InvalidPromptError import InvalidPromptError
from language_model import LanguageModel
from model_type import ModelType


class LlamaModel(LanguageModel):
    def __init__(self, model_name: str, provider: str, max_tokens: int, temperature: float, model_path: str, quantization: str, model_type: ModelType):
        super().__init__(model_name, provider, max_tokens, temperature, model_type)
        self.model_path = model_path
        self.quantization = quantization
        self.model_type = self.model_type

    def generate_response(self, query):
        if not self.isPromptValid(query):
            raise InvalidPromptError
        return f'Local Llama API response to: {query}\nInput Tokens: {self.tokenizer.count_tokens(query)}'