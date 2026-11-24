from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockBatchDeleteAdvancedPromptOptimizationJobRequest(BaseModel):
    jobIdentifiers: list[StrictStr]
