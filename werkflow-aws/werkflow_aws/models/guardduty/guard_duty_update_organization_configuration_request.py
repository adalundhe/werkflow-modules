from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .guard_duty_organization_data_source_configurations import GuardDutyOrganizationDataSourceConfigurations
from .guard_duty_organization_feature_configuration import GuardDutyOrganizationFeatureConfiguration


class GuardDutyUpdateOrganizationConfigurationRequest(BaseModel):
    DetectorId: StrictStr
    AutoEnable: StrictBool | None = None
    DataSources: GuardDutyOrganizationDataSourceConfigurations | None = None
    Features: list[GuardDutyOrganizationFeatureConfiguration] | None = None
    AutoEnableOrganizationMembers: Literal['NEW', 'ALL', 'NONE'] | None = None
