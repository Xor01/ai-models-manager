class Tokenizer:
    """Class to define the tokenizer for a language model."""
    def count_tokens(self, text: str):
        return len(text.split())