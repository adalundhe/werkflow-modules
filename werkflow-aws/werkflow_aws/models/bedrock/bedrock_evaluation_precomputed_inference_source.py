from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationPrecomputedInferenceSource(BaseModel):
    inferenceSourceIdentifier: StrictStr | None = None
