from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeThrottlingException(BaseModel):
    message: StrictStr | None = None
