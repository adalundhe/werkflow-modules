from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class ConnectEvaluationScore(BaseModel):
    Percentage: StrictFloat | StrictInt | None = None
    NotApplicable: StrictBool | None = None
    AutomaticFail: StrictBool | None = None
    AppliedWeight: StrictFloat | StrictInt | None = None
    EarnedPoints: StrictInt | None = None
    MaxBasePoint: StrictInt | None = None
    PerformanceCategory: StrictStr | None = None
