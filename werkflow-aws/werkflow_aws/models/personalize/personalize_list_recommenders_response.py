from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_recommender_summary import PersonalizeRecommenderSummary


class PersonalizeListRecommendersResponse(BaseModel):
    recommenders: list[PersonalizeRecommenderSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
