from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_usage_limit import RedshiftUsageLimit


class RedshiftDescribeUsageLimitsResponse(BaseModel):
    UsageLimits: list[RedshiftUsageLimit] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
