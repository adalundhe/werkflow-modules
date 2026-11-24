from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation


class SSMAssociationExecution(BaseModel):
    AssociationId: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
    ExecutionId: StrictStr | None = None
    Status: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastExecutionDate: datetime.datetime | StrictStr | None = None
    ResourceCountByStatus: StrictStr | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
