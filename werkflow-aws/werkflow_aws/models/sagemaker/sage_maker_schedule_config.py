from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerScheduleConfig(BaseModel):
    ScheduleExpression: StrictStr | None = None
    DataAnalysisStartTime: StrictStr | None = None
    DataAnalysisEndTime: StrictStr | None = None
