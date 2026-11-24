from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class BedrockRoutingCriteria(BaseModel):
    responseQualityDifference: StrictFloat | StrictInt | None = None
