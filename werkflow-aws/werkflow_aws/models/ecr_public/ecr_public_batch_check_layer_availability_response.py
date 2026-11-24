from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_layer import ECRPublicLayer
from .ecr_public_layer_failure import ECRPublicLayerFailure


class ECRPublicBatchCheckLayerAvailabilityResponse(BaseModel):
    layers: list[ECRPublicLayer] | None = None
    failures: list[ECRPublicLayerFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
