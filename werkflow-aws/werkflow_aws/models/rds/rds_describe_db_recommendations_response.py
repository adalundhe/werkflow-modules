from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_recommendation import RDSDBRecommendation


class RDSDescribeDBRecommendationsResponse(BaseModel):
    DBRecommendations: list[RDSDBRecommendation] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
