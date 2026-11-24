from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_column_statistics_error import GlueColumnStatisticsError


class GlueUpdateColumnStatisticsForPartitionResponse(BaseModel):
    Errors: list[GlueColumnStatisticsError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
