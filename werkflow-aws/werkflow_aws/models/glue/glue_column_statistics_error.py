from __future__ import annotations
from pydantic import BaseModel
from .glue_column_statistics import GlueColumnStatistics
from .glue_error_detail import GlueErrorDetail


class GlueColumnStatisticsError(BaseModel):
    ColumnStatistics: GlueColumnStatistics | None = None
    Error: GlueErrorDetail | None = None
