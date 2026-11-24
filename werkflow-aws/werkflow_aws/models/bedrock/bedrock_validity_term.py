from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockValidityTerm(BaseModel):
    agreementDuration: StrictStr | None = None
