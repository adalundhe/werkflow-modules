from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_license_configuration import ComputeOptimizerLicenseConfiguration
from .compute_optimizer_license_recommendation_option import ComputeOptimizerLicenseRecommendationOption
from .compute_optimizer_tag import ComputeOptimizerTag


class ComputeOptimizerLicenseRecommendation(BaseModel):
    resourceArn: StrictStr | None = None
    accountId: StrictStr | None = None
    currentLicenseConfiguration: ComputeOptimizerLicenseConfiguration | None = None
    lookbackPeriodInDays: StrictFloat | StrictInt | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    finding: StrictStr | None = None
    findingReasonCodes: list[StrictStr] | None = None
    licenseRecommendationOptions: list[ComputeOptimizerLicenseRecommendationOption] | None = None
    tags: list[ComputeOptimizerTag] | None = None
