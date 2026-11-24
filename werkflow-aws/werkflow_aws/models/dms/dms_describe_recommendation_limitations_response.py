from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_limitation import DMSLimitation


class DMSDescribeRecommendationLimitationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Limitations: list[DMSLimitation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
