from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_ebs_filter import ComputeOptimizerEBSFilter


class ComputeOptimizerGetEBSVolumeRecommendationsRequest(BaseModel):
    volumeArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerEBSFilter] | None = None
    accountIds: list[StrictStr] | None = None
