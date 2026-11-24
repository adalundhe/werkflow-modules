from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .step_functions_encryption_configuration import StepFunctionsEncryptionConfiguration
from .step_functions_logging_configuration import StepFunctionsLoggingConfiguration
from .step_functions_tracing_configuration import StepFunctionsTracingConfiguration


class StepFunctionsUpdateStateMachineRequest(BaseModel):
    stateMachineArn: StrictStr
    definition: StrictStr | None = None
    roleArn: StrictStr | None = None
    loggingConfiguration: StepFunctionsLoggingConfiguration | None = None
    tracingConfiguration: StepFunctionsTracingConfiguration | None = None
    publish: StrictBool | None = None
    versionDescription: StrictStr | None = None
    encryptionConfiguration: StepFunctionsEncryptionConfiguration | None = None
