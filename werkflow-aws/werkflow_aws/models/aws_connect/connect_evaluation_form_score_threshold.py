from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectEvaluationFormScoreThreshold(BaseModel):
    PerformanceCategory: StrictStr | None = None
    MinScorePercentage: StrictFloat | StrictInt | None = None
    MaxScorePercentage: StrictFloat | StrictInt | None = None
