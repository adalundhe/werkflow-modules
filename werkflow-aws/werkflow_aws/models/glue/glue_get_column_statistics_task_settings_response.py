from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_column_statistics_task_settings import GlueColumnStatisticsTaskSettings


class GlueGetColumnStatisticsTaskSettingsResponse(BaseModel):
    ColumnStatisticsTaskSettings: GlueColumnStatisticsTaskSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
