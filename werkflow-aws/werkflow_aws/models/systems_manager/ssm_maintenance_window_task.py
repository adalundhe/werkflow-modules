from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_logging_info import SSMLoggingInfo
from .ssm_maintenance_window_task_parameter_value_expression import SSMMaintenanceWindowTaskParameterValueExpression
from .ssm_target import SSMTarget


class SSMMaintenanceWindowTask(BaseModel):
    WindowId: StrictStr | None = None
    WindowTaskId: StrictStr | None = None
    TaskArn: StrictStr | None = None
    Type: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    TaskParameters: dict[StrictStr, SSMMaintenanceWindowTaskParameterValueExpression] | None = None
    Priority: StrictInt | None = None
    LoggingInfo: SSMLoggingInfo | None = None
    ServiceRoleArn: StrictStr | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CutoffBehavior: StrictStr | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
