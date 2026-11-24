from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetRecommenderConfigurationRequest(BaseModel):
    RecommenderId: StrictStr
