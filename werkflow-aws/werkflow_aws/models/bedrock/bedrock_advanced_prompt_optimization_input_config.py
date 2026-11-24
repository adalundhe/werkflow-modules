from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAdvancedPromptOptimizationInputConfig(BaseModel):
    s3Uri: StrictStr | None = None
