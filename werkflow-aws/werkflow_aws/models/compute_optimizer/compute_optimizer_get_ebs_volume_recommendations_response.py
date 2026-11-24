from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_get_recommendation_error import ComputeOptimizerGetRecommendationError
from .compute_optimizer_volume_recommendation import ComputeOptimizerVolumeRecommendation


class ComputeOptimizerGetEBSVolumeRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    volumeRecommendations: list[ComputeOptimizerVolumeRecommendation] | None = None
    errors: list[ComputeOptimizerGetRecommendationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
