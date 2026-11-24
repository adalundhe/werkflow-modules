from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_target import SSMTarget


class SSMTargetLocation(BaseModel):
    Accounts: list[StrictStr] | None = None
    Regions: list[StrictStr] | None = None
    TargetLocationMaxConcurrency: StrictStr | None = None
    TargetLocationMaxErrors: StrictStr | None = None
    ExecutionRoleName: StrictStr | None = None
    TargetLocationAlarmConfiguration: SSMAlarmConfiguration | None = None
    IncludeChildOrganizationUnits: StrictBool | None = None
    ExcludeAccounts: list[StrictStr] | None = None
    Targets: list[SSMTarget] | None = None
    TargetsMaxConcurrency: StrictStr | None = None
    TargetsMaxErrors: StrictStr | None = None
