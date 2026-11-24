from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_alarm_configuration import SSMAlarmConfiguration
from .ssm_logging_info import SSMLoggingInfo
from .ssm_maintenance_window_task_invocation_parameters import SSMMaintenanceWindowTaskInvocationParameters
from .ssm_maintenance_window_task_parameter_value_expression import SSMMaintenanceWindowTaskParameterValueExpression
from .ssm_target import SSMTarget


class SSMGetMaintenanceWindowTaskResponse(BaseModel):
    WindowId: StrictStr | None = None
    WindowTaskId: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    TaskArn: StrictStr | None = None
    ServiceRoleArn: StrictStr | None = None
    TaskType: StrictStr | None = None
    TaskParameters: dict[StrictStr, SSMMaintenanceWindowTaskParameterValueExpression] | None = None
    TaskInvocationParameters: SSMMaintenanceWindowTaskInvocationParameters | None = None
    Priority: StrictInt | None = None
    MaxConcurrency: StrictStr | None = None
    MaxErrors: StrictStr | None = None
    LoggingInfo: SSMLoggingInfo | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CutoffBehavior: StrictStr | None = None
    AlarmConfiguration: SSMAlarmConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
