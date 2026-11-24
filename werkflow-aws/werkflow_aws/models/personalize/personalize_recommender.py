from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .personalize_recommender_config import PersonalizeRecommenderConfig
from .personalize_recommender_update_summary import PersonalizeRecommenderUpdateSummary


class PersonalizeRecommender(BaseModel):
    recommenderArn: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    name: StrictStr | None = None
    recipeArn: StrictStr | None = None
    recommenderConfig: PersonalizeRecommenderConfig | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    failureReason: StrictStr | None = None
    latestRecommenderUpdate: PersonalizeRecommenderUpdateSummary | None = None
    modelMetrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
