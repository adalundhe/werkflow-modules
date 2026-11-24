from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_organization_additional_configuration_result import GuardDutyOrganizationAdditionalConfigurationResult


class GuardDutyOrganizationFeatureConfigurationResult(BaseModel):
    Name: StrictStr | None = None
    AutoEnable: StrictStr | None = None
    AdditionalConfiguration: list[GuardDutyOrganizationAdditionalConfigurationResult] | None = None
