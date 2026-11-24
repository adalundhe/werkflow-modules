from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FMSEvaluationResult(BaseModel):
    ComplianceStatus: StrictStr | None = None
    ViolatorCount: StrictInt | None = None
    EvaluationLimitExceeded: StrictBool | None = None
