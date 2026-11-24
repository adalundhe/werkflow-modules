from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_recommender_config import PersonalizeRecommenderConfig


class PersonalizeUpdateRecommenderRequest(BaseModel):
    recommenderArn: StrictStr
    recommenderConfig: PersonalizeRecommenderConfig
