from __future__ import annotations
from pydantic import BaseModel
from .bedrock_legal_term import BedrockLegalTerm
from .bedrock_pricing_term import BedrockPricingTerm
from .bedrock_support_term import BedrockSupportTerm
from .bedrock_validity_term import BedrockValidityTerm


class BedrockTermDetails(BaseModel):
    usageBasedPricingTerm: BedrockPricingTerm | None = None
    legalTerm: BedrockLegalTerm | None = None
    supportTerm: BedrockSupportTerm | None = None
    validityTerm: BedrockValidityTerm | None = None
