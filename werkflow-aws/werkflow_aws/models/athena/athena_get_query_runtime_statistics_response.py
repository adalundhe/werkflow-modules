from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_query_runtime_statistics import AthenaQueryRuntimeStatistics


class AthenaGetQueryRuntimeStatisticsResponse(BaseModel):
    QueryRuntimeStatistics: AthenaQueryRuntimeStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
