from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGuardrailTopicsTier(BaseModel):
    tierName: StrictStr | None = None
