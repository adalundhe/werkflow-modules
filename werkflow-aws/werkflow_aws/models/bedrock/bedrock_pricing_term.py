from __future__ import annotations
from pydantic import BaseModel
from .bedrock_dimensional_price_rate import BedrockDimensionalPriceRate


class BedrockPricingTerm(BaseModel):
    rateCard: list[BedrockDimensionalPriceRate] | None = None
