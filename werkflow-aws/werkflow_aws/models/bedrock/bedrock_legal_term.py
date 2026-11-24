from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockLegalTerm(BaseModel):
    url: StrictStr | None = None
