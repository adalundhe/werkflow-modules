from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_recommendation import DMSRecommendation


class DMSDescribeRecommendationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Recommendations: list[DMSRecommendation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
