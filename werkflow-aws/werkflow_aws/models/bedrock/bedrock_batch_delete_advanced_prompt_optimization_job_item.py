from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockBatchDeleteAdvancedPromptOptimizationJobItem(BaseModel):
    jobIdentifier: StrictStr | None = None
    jobStatus: StrictStr | None = None
