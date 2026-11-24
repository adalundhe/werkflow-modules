from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .personalize_recommender_config import PersonalizeRecommenderConfig


class PersonalizeRecommenderUpdateSummary(BaseModel):
    recommenderConfig: PersonalizeRecommenderConfig | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    failureReason: StrictStr | None = None
