from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGuardrailContextualGroundingTier(BaseModel):
    tierName: StrictStr | None = None
