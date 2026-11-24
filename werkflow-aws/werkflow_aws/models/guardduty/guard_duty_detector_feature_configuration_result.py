from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_detector_additional_configuration_result import GuardDutyDetectorAdditionalConfigurationResult


class GuardDutyDetectorFeatureConfigurationResult(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    AdditionalConfiguration: list[GuardDutyDetectorAdditionalConfigurationResult] | None = None
    ManagedBy: StrictStr | None = None
