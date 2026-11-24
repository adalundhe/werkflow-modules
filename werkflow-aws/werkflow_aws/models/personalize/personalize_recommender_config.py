from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .personalize_training_data_config import PersonalizeTrainingDataConfig


class PersonalizeRecommenderConfig(BaseModel):
    itemExplorationConfig: dict[StrictStr, StrictStr] | None = None
    minRecommendationRequestsPerSecond: StrictInt | None = None
    trainingDataConfig: PersonalizeTrainingDataConfig | None = None
    enableMetadataWithRecommendations: StrictBool | None = None
