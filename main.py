from InvalidPromptError import InvalidPromptError
from conversation import Conversation
from models.GPTModel import GPTModel
from models.LlamaModel import LlamaModel
from pricing_plan import PricingPlan
from model_manager import ModelManager

def main():
    basic_pricing = PricingPlan("Basic", 10)
    gpt_model = GPTModel('GPT-5.4', 'openai', 10000, 0, 'top_secret', basic_pricing)
    llama_model = LlamaModel('Llama-3', "Meta", 1000, 1.3, 'path/to/model', '4bit')
    model_manager = ModelManager()

    model_manager.add_model(gpt_model)
    model_manager.add_model(llama_model)
    conversation = Conversation(conversation_id=1,model=gpt_model)
    conversation.send_message("Explain object-oriented programming")
    conversation.display_history()
    
    
if __name__ == "__main__":
    main()
