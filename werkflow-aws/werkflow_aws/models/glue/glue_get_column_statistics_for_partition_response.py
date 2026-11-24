from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_column_error import GlueColumnError
from .glue_column_statistics import GlueColumnStatistics


class GlueGetColumnStatisticsForPartitionResponse(BaseModel):
    ColumnStatisticsList: list[GlueColumnStatistics] | None = None
    Errors: list[GlueColumnError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
