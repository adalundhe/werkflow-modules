from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeInternalServerException(BaseModel):
    message: StrictStr | None = None
