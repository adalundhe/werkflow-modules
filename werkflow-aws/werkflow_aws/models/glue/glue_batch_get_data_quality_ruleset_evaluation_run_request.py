from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetDataQualityRulesetEvaluationRunRequest(BaseModel):
    RunIds: list[StrictStr]
