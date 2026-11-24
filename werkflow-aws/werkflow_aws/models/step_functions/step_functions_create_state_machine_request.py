from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .step_functions_encryption_configuration import StepFunctionsEncryptionConfiguration
from .step_functions_logging_configuration import StepFunctionsLoggingConfiguration
from .step_functions_tag import StepFunctionsTag
from .step_functions_tracing_configuration import StepFunctionsTracingConfiguration


class StepFunctionsCreateStateMachineRequest(BaseModel):
    name: StrictStr
    definition: StrictStr
    roleArn: StrictStr
    type: Literal['STANDARD', 'EXPRESS'] | None = None
    loggingConfiguration: StepFunctionsLoggingConfiguration | None = None
    tags: list[StepFunctionsTag] | None = None
    tracingConfiguration: StepFunctionsTracingConfiguration | None = None
    publish: StrictBool | None = None
    versionDescription: StrictStr | None = None
    encryptionConfiguration: StepFunctionsEncryptionConfiguration | None = None
