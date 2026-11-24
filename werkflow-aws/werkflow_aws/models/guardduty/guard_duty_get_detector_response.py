from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_data_source_configurations_result import GuardDutyDataSourceConfigurationsResult
from .guard_duty_detector_feature_configuration_result import GuardDutyDetectorFeatureConfigurationResult


class GuardDutyGetDetectorResponse(BaseModel):
    CreatedAt: StrictStr | None = None
    FindingPublishingFrequency: StrictStr | None = None
    ServiceRole: StrictStr | None = None
    Status: StrictStr | None = None
    UpdatedAt: StrictStr | None = None
    DataSources: GuardDutyDataSourceConfigurationsResult | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Features: list[GuardDutyDetectorFeatureConfigurationResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
