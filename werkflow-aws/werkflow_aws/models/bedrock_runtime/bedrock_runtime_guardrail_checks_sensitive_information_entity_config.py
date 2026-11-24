from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailChecksSensitiveInformationEntityConfig(BaseModel):
    type: StrictStr
