from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_license_recommendation_filter import ComputeOptimizerLicenseRecommendationFilter


class ComputeOptimizerGetLicenseRecommendationsRequest(BaseModel):
    resourceArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerLicenseRecommendationFilter] | None = None
    accountIds: list[StrictStr] | None = None
