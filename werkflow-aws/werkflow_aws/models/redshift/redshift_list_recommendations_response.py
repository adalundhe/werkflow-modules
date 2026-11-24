from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_recommendation import RedshiftRecommendation


class RedshiftListRecommendationsResponse(BaseModel):
    Recommendations: list[RedshiftRecommendation] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
