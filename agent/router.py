
class ModelRouter:

    def select_model(self, complexity: str):

        routing_rules = {
            "SIMPLE": {
                "tier": "LOW_COST",
                "reason": "Simple task requires fewer resources"
            },
            "MEDIUM": {
                "tier": "BALANCED",
                "reason": "Moderate reasoning is required"
            },
            "COMPLEX": {
                "tier": "HIGH_CAPABILITY",
                "reason": "Complex reasoning is required"
            }
        }

        if complexity not in routing_rules:
            raise ValueError("Unknown task complexity")

        return routing_rules[complexity]
