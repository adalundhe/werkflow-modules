from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_guard_duty_detector_data_sources_details import SecurityHubAwsGuardDutyDetectorDataSourcesDetails
from .security_hub_aws_guard_duty_detector_features_details import SecurityHubAwsGuardDutyDetectorFeaturesDetails


class SecurityHubAwsGuardDutyDetectorDetails(BaseModel):
    DataSources: SecurityHubAwsGuardDutyDetectorDataSourcesDetails | None = None
    Features: list[SecurityHubAwsGuardDutyDetectorFeaturesDetails] | None = None
    FindingPublishingFrequency: StrictStr | None = None
    ServiceRole: StrictStr | None = None
    Status: StrictStr | None = None
