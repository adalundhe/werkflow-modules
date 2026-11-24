from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .personalize_recommender_config import PersonalizeRecommenderConfig


class PersonalizeRecommenderSummary(BaseModel):
    name: StrictStr | None = None
    recommenderArn: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    recipeArn: StrictStr | None = None
    recommenderConfig: PersonalizeRecommenderConfig | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
