from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_step_function_state_machine_logging_configuration_details import SecurityHubAwsStepFunctionStateMachineLoggingConfigurationDetails
from .security_hub_aws_step_function_state_machine_tracing_configuration_details import SecurityHubAwsStepFunctionStateMachineTracingConfigurationDetails


class SecurityHubAwsStepFunctionStateMachineDetails(BaseModel):
    Label: StrictStr | None = None
    LoggingConfiguration: SecurityHubAwsStepFunctionStateMachineLoggingConfigurationDetails | None = None
    Name: StrictStr | None = None
    RoleArn: StrictStr | None = None
    StateMachineArn: StrictStr | None = None
    Status: StrictStr | None = None
    TracingConfiguration: SecurityHubAwsStepFunctionStateMachineTracingConfigurationDetails | None = None
    Type: StrictStr | None = None
