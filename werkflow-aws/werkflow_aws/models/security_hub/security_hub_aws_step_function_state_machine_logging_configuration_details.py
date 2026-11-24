from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_step_function_state_machine_logging_configuration_destinations_details import SecurityHubAwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails


class SecurityHubAwsStepFunctionStateMachineLoggingConfigurationDetails(BaseModel):
    Destinations: list[SecurityHubAwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails] | None = None
    IncludeExecutionData: StrictBool | None = None
    Level: StrictStr | None = None
