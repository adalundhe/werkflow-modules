from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyBuildStepMessage(BaseModel):
    message: StrictStr | None = None
    messageType: StrictStr | None = None
