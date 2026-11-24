from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationModelConfigSummary(BaseModel):
    bedrockModelIdentifiers: list[StrictStr] | None = None
    precomputedInferenceSourceIdentifiers: list[StrictStr] | None = None
