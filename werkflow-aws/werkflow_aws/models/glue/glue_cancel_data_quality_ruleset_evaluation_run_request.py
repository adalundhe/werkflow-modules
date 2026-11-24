from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCancelDataQualityRulesetEvaluationRunRequest(BaseModel):
    RunId: StrictStr
