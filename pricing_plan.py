class PricingPlan:
    """Class to define the pricing plan for a language model."""
    def __init__(self, plan_name: str, price_per_1000_tokens: float):
        self.plan_name = plan_name
        self.price_per_1000_tokens = price_per_1000_tokens


    def calculate_cost(self, num_tokens: int):
        return (num_tokens / 1000) * self.price_per_1000_tokens