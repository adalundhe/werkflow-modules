from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeCitationSourceContent(BaseModel):
    text: StrictStr | None = None
