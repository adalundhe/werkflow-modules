from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_layer import ECRLayer
from .ecr_layer_failure import ECRLayerFailure


class ECRBatchCheckLayerAvailabilityResponse(BaseModel):
    layers: list[ECRLayer] | None = None
    failures: list[ECRLayerFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
