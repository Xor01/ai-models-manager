from abc import ABC, abstractmethod
from model_type import ModelType
from tokenizer import Tokenizer

class LanguageModel(ABC):
    """Abstract base class to define the structure of a language model."""
    
    total_models = 0
    def __init__(self, model_name: str, provider: str, max_tokens: int, temperature: float, model_type: ModelType):
        self.model_name = model_name
        self.provider = provider
        self.max_tokens = max_tokens
        self.__temperature = temperature
        LanguageModel.total_models +=1
        self.tokenizer = Tokenizer()
        self.__is_active = True
        self.model_type = model_type


    @property
    def is_active(self):
        return self.__is_active
    
    @is_active.setter
    def is_active(self):
        return self.__is_active
    

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        if (self.validate_temperature(value)):
            self.__temperature = value
        else:
            return ValueError(f'{value} is outside of constraint') 


    @classmethod
    def get_total_models():
        return LanguageModel.total_models
    

    def isPromptValid(self, prompt: str):
        if not isinstance(prompt, str):
            return False
        if len(prompt) == 0:
            return False
        if prompt.isspace():
            return False
        return True
    def __str__(self):
        return f"""
Model Name: {self.model_name}
Provider: {self.provider}
Max Tokens: {self.max_tokens}
Temperature: {self.temperature}
""".strip()
    
    @abstractmethod
    def generate_response(query: str):
        return f'Base Model Response'
    
    def display_info(self):
        print(f"""
Model Name: {self.model_name}
Provider: {self.provider}
Max Tokens: {self.max_tokens}
Temperature: {self.temperature}
""".strip())
    
    @staticmethod
    def validate_temperature(temperature: float):
        return   0.0 <= temperature <= 2.0
    