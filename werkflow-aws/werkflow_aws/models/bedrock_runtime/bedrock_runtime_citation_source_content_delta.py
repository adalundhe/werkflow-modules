from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeCitationSourceContentDelta(BaseModel):
    text: StrictStr | None = None
