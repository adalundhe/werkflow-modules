from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_recommender_config import PersonalizeRecommenderConfig
from .personalize_tag import PersonalizeTag


class PersonalizeCreateRecommenderRequest(BaseModel):
    name: StrictStr
    datasetGroupArn: StrictStr
    recipeArn: StrictStr
    recommenderConfig: PersonalizeRecommenderConfig | None = None
    tags: list[PersonalizeTag] | None = None
