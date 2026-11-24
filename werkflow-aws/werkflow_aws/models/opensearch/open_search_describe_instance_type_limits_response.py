from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_limits import OpenSearchLimits


class OpenSearchDescribeInstanceTypeLimitsResponse(BaseModel):
    LimitsByRole: dict[StrictStr, OpenSearchLimits] | None = None
    ResponseMetadata: dict[str, Any] | None = None
