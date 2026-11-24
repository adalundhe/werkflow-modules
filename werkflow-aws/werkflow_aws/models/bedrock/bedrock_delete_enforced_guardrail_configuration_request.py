from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeleteEnforcedGuardrailConfigurationRequest(BaseModel):
    configId: StrictStr
