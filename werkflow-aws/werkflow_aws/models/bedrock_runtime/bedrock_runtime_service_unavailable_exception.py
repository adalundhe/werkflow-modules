from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeServiceUnavailableException(BaseModel):
    message: StrictStr | None = None
