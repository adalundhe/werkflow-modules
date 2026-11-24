from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeModelTimeoutException(BaseModel):
    message: StrictStr | None = None
