from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_list_recommender_configurations_response import PinpointListRecommenderConfigurationsResponse


class PinpointGetRecommenderConfigurationsResponse(BaseModel):
    ListRecommenderConfigurationsResponse: PinpointListRecommenderConfigurationsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
