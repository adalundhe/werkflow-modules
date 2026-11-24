from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation


class SSMMaintenanceWindowExecutionTaskIdentity(BaseModel):
    WindowExecutionId: StrictStr | None = None
    TaskExecutionId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    TaskArn: StrictStr | None = None
    TaskType: StrictStr | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
