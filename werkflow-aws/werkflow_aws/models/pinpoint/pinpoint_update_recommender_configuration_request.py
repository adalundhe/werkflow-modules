from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_update_recommender_configuration import PinpointUpdateRecommenderConfiguration


class PinpointUpdateRecommenderConfigurationRequest(BaseModel):
    RecommenderId: StrictStr
    UpdateRecommenderConfiguration: PinpointUpdateRecommenderConfiguration
