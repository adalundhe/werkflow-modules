from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockListEnforcedGuardrailsConfigurationRequest(BaseModel):
    nextToken: StrictStr | None = None
