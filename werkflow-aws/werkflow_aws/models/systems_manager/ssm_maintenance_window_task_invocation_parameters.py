from __future__ import annotations
from pydantic import BaseModel
from .ssm_maintenance_window_automation_parameters import SSMMaintenanceWindowAutomationParameters
from .ssm_maintenance_window_lambda_parameters import SSMMaintenanceWindowLambdaParameters
from .ssm_maintenance_window_run_command_parameters import SSMMaintenanceWindowRunCommandParameters
from .ssm_maintenance_window_step_functions_parameters import SSMMaintenanceWindowStepFunctionsParameters


class SSMMaintenanceWindowTaskInvocationParameters(BaseModel):
    RunCommand: SSMMaintenanceWindowRunCommandParameters | None = None
    Automation: SSMMaintenanceWindowAutomationParameters | None = None
    StepFunctions: SSMMaintenanceWindowStepFunctionsParameters | None = None
    Lambda: SSMMaintenanceWindowLambdaParameters | None = None
