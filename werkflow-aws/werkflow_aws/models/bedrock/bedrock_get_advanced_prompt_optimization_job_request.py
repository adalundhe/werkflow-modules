from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetAdvancedPromptOptimizationJobRequest(BaseModel):
    jobIdentifier: StrictStr
