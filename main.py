from InvalidPromptError import InvalidPromptError
from conversation import Conversation
from embeddings_model import EmbeddingModel
from model_manager import ModelManager
from model_type import ModelType
from models.GPTModel import GPTModel
from models.LlamaModel import LlamaModel
from pricing_plan import PricingPlan


def main():
    premium_pricing = PricingPlan("Premium", 100)
    gpt = GPTModel("GPT-5.4", "openai", 500000, 0.1, 'top_secret', premium_pricing, ModelType.CHAT)
    llama = LlamaModel("Llama-01", "Meta", 500, 0.2, 'path/to/model', "4bit", ModelType.CHAT)
    models = [gpt, llama]
    for model in models:
        try:
            print(model.generate_response("Explain OOP"))
        except InvalidPromptError as e:
            print(e)
    try:
        print(gpt.generate_response(""))
    except InvalidPromptError:
        print('Invalid Prompt')

    
    print("*" * 30)

    basic_pricing = PricingPlan("Basic", 10)
    gpt_model = GPTModel('GPT-5.4', 'openai', 10000, 0, 'top_secret', basic_pricing, ModelType.CHAT)
    llama_model = LlamaModel('Llama-3', "Meta", 1000, 1.3, 'path/to/model', '4bit', ModelType.CHAT)
    model_manager = ModelManager()

    model_manager.add_model(gpt_model)
    model_manager.add_model(llama_model)

    embeddings_model = EmbeddingModel('gpt-embeddings-3-small', 'openai', 1000, 0, ModelType.EMBEDDINGS)
    model_manager.add_model(embeddings_model)
    conversation = Conversation(conversation_id=1,model=gpt_model)
    conversation.send_message("Explain object-oriented programming")
    conversation.display_history()

    embeddings_conversation = Conversation(conversation_id=2, model=embeddings_model)
    embeddings_conversation.send_message("Hello, World")
    embeddings_conversation.display_history()
    
if __name__ == "__main__":
    main()
