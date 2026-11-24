from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_alarm_state_information import SSMAlarmStateInformation
from .ssm_maintenance_window_task_parameter_value_expression import SSMMaintenanceWindowTaskParameterValueExpression


class SSMGetMaintenanceWindowExecutionTaskResponse(BaseModel):
    WindowExecutionId: StrictStr | None = None
    TaskExecutionId: StrictStr | None = None
    TaskArn: StrictStr | None = None
    ServiceRole: StrictStr | None = None
    Type: StrictStr | None = None
    TaskParameters: list[dict[StrictStr, SSMMaintenanceWindowTaskParameterValueExpression]] | None = None
    Priority: StrictInt | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    TriggeredAlarms: list[SSMAlarmStateInformation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
