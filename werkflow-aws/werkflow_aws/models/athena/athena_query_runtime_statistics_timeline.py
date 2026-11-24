from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AthenaQueryRuntimeStatisticsTimeline(BaseModel):
    QueryQueueTimeInMillis: StrictInt | None = None
    ServicePreProcessingTimeInMillis: StrictInt | None = None
    QueryPlanningTimeInMillis: StrictInt | None = None
    EngineExecutionTimeInMillis: StrictInt | None = None
    ServiceProcessingTimeInMillis: StrictInt | None = None
    TotalExecutionTimeInMillis: StrictInt | None = None
