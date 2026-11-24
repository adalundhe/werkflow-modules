from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeServiceUpdatesRequest(BaseModel):
    ServiceUpdateName: StrictStr | None = None
    ServiceUpdateStatus: list[Literal['available', 'cancelled', 'expired']] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
