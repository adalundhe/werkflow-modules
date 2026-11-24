from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockProjectDataRetention(BaseModel):
    mode: StrictStr | None = None
