from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ecr_transitioning_image_total_count import ECRTransitioningImageTotalCount


class ECRLifecyclePolicyPreviewSummary(BaseModel):
    expiringImageTotalCount: StrictInt | None = None
    transitioningImageTotalCounts: list[ECRTransitioningImageTotalCount] | None = None
