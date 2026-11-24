from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from .location_positional_accuracy import LocationPositionalAccuracy


class LocationInferredState(BaseModel):
    Position: list[StrictFloat | StrictInt] | None = None
    Accuracy: LocationPositionalAccuracy | None = None
    DeviationDistance: StrictFloat | StrictInt | None = None
    ProxyDetected: StrictBool | None = None
