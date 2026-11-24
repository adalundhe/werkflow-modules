from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_column_statistics_task_run import GlueColumnStatisticsTaskRun


class GlueGetColumnStatisticsTaskRunResponse(BaseModel):
    ColumnStatisticsTaskRun: GlueColumnStatisticsTaskRun | None = None
    ResponseMetadata: dict[str, Any] | None = None
