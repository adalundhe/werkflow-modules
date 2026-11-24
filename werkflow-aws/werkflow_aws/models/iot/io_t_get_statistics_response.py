from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_statistics import IoTStatistics


class IoTGetStatisticsResponse(BaseModel):
    statistics: IoTStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
