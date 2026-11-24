from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LocationCalculateRouteCarModeOptions(BaseModel):
    AvoidFerries: StrictBool | None = None
    AvoidTolls: StrictBool | None = None
