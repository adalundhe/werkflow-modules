from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeValidationException(BaseModel):
    message: StrictStr | None = None
