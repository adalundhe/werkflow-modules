from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBedrockGuardrailConfiguration(BaseModel):
    identifier: StrictStr | None = None
    version: StrictStr | None = None
