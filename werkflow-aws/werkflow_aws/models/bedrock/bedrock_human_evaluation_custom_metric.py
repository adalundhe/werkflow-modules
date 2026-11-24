from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockHumanEvaluationCustomMetric(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    ratingMethod: StrictStr | None = None
