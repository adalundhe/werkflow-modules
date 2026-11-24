from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockSupportTerm(BaseModel):
    refundPolicyDescription: StrictStr | None = None
