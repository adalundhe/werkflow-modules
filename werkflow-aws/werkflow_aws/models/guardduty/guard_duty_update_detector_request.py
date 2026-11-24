from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .guard_duty_data_source_configurations import GuardDutyDataSourceConfigurations
from .guard_duty_detector_feature_configuration import GuardDutyDetectorFeatureConfiguration


class GuardDutyUpdateDetectorRequest(BaseModel):
    DetectorId: StrictStr
    Enable: StrictBool | None = None
    FindingPublishingFrequency: Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS'] | None = None
    DataSources: GuardDutyDataSourceConfigurations | None = None
    Features: list[GuardDutyDetectorFeatureConfiguration] | None = None
