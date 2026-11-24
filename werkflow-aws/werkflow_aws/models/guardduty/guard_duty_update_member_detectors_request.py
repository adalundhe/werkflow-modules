from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_data_source_configurations import GuardDutyDataSourceConfigurations
from .guard_duty_member_features_configuration import GuardDutyMemberFeaturesConfiguration


class GuardDutyUpdateMemberDetectorsRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
    DataSources: GuardDutyDataSourceConfigurations | None = None
    Features: list[GuardDutyMemberFeaturesConfiguration] | None = None
