from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_logging_info import SSMLoggingInfo
from .ssm_maintenance_window_task_invocation_parameters import SSMMaintenanceWindowTaskInvocationParameters
from .ssm_maintenance_window_task_parameter_value_expression import SSMMaintenanceWindowTaskParameterValueExpression
from .ssm_target import SSMTarget


class SSMUpdateMaintenanceWindowTaskRequest(BaseModel):
    WindowId: StrictStr
    WindowTaskId: StrictStr
    Targets: list[SSMTarget] | None = None
    TaskArn: StrictStr | None = None
    ServiceRoleArn: StrictStr | None = None
    TaskParameters: dict[StrictStr, SSMMaintenanceWindowTaskParameterValueExpression] | None = None
    TaskInvocationParameters: SSMMaintenanceWindowTaskInvocationParameters | None = None
    Priority: StrictInt | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    LoggingInfo: SSMLoggingInfo | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Replace: StrictBool | None = None
    CutoffBehavior: Literal['CONTINUE_TASK', 'CANCEL_TASK'] | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
