from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_recommender_configuration_response import PinpointRecommenderConfigurationResponse


class PinpointDeleteRecommenderConfigurationResponse(BaseModel):
    RecommenderConfigurationResponse: PinpointRecommenderConfigurationResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
