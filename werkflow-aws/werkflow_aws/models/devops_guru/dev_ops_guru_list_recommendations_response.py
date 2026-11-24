from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_recommendation import DevOpsGuruRecommendation


class DevOpsGuruListRecommendationsResponse(BaseModel):
    Recommendations: list[DevOpsGuruRecommendation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
