from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockCustomMetricBedrockEvaluatorModel(BaseModel):
    modelIdentifier: StrictStr | None = None
