from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceGetResourceEvaluationSummaryRequest(BaseModel):
    ResourceEvaluationId: StrictStr
