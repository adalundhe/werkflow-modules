from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_batch_evaluate_geofences_error import LocationBatchEvaluateGeofencesError


class LocationBatchEvaluateGeofencesResponse(BaseModel):
    Errors: list[LocationBatchEvaluateGeofencesError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
