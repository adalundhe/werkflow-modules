from __future__ import annotations
from pydantic import BaseModel
from .athena_query_runtime_statistics_rows import AthenaQueryRuntimeStatisticsRows
from .athena_query_runtime_statistics_timeline import AthenaQueryRuntimeStatisticsTimeline
from .athena_query_stage import AthenaQueryStage


class AthenaQueryRuntimeStatistics(BaseModel):
    Timeline: AthenaQueryRuntimeStatisticsTimeline | None = None
    Rows: AthenaQueryRuntimeStatisticsRows | None = None
    OutputStage: AthenaQueryStage | None = None
