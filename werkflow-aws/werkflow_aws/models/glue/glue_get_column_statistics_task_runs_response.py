from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_column_statistics_task_run import GlueColumnStatisticsTaskRun


class GlueGetColumnStatisticsTaskRunsResponse(BaseModel):
    ColumnStatisticsTaskRuns: list[GlueColumnStatisticsTaskRun] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
