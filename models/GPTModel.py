from InvalidPromptError import InvalidPromptError
from LoggingMixin import LoggingMixin
from language_model import LanguageModel


class GPTModel(LanguageModel, LoggingMixin):

    def __init__(self, model_name: str, provider: str, max_tokens: int, temperature: int, api_key: str, pricing_plan=None):
        super().__init__(model_name, provider, max_tokens, temperature)
        self.api_key = api_key
        self.pricing_plan = pricing_plan

    def generate_response(self, query):
        if not self.isPromptValid(query):
            raise InvalidPromptError
        self.log('Sending request to GPT-Model')
        return f'GPT API response to: {query}\nInput Tokens: {self.tokenizer.count_tokens(query)}'  
    
    def calculate_request_cost(self, query):
        if self.pricing_plan:
            num_tokens = self.tokenizer.count_tokens(query)
            return self.pricing_plan.calculate_cost(num_tokens)
        else:
            return None
        
    def __str__(self):
        return 'GPT-Model by OpenAI'
    
    def __repr__(self):
        return f"GPTModel(model_name='{self.model_name}', provider='{self.provider}')"
    
    def __len__(self):
        return self.max_tokens
    
    def __eq__(self, other):
        if not other.isinstance(LanguageModel):
            return False
        if(self.model_name == other.model_name & self.provider == other.provider):
            return True
    
        return False