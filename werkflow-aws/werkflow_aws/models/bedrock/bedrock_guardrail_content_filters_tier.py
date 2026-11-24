from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGuardrailContentFiltersTier(BaseModel):
    tierName: StrictStr | None = None
