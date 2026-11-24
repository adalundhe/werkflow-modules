from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_recommender_configuration_response import PinpointRecommenderConfigurationResponse


class PinpointListRecommenderConfigurationsResponse(BaseModel):
    Item: list[PinpointRecommenderConfigurationResponse] | None = None
    NextToken: StrictStr | None = None
