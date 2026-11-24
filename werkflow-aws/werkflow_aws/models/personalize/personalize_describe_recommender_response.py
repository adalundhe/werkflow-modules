from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_recommender import PersonalizeRecommender


class PersonalizeDescribeRecommenderResponse(BaseModel):
    recommender: PersonalizeRecommender | None = None
    ResponseMetadata: dict[str, Any] | None = None
