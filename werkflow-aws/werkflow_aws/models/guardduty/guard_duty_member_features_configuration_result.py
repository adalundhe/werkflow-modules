from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_member_additional_configuration_result import GuardDutyMemberAdditionalConfigurationResult


class GuardDutyMemberFeaturesConfigurationResult(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    AdditionalConfiguration: list[GuardDutyMemberAdditionalConfigurationResult] | None = None
    ManagedBy: StrictStr | None = None
