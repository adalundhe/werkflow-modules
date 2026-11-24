from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteRecommenderConfigurationRequest(BaseModel):
    RecommenderId: StrictStr
