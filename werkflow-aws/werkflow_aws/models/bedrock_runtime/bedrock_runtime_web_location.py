from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeWebLocation(BaseModel):
    url: StrictStr | None = None
    domain: StrictStr | None = None
