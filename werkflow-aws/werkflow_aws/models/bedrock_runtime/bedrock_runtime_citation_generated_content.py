from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeCitationGeneratedContent(BaseModel):
    text: StrictStr | None = None
