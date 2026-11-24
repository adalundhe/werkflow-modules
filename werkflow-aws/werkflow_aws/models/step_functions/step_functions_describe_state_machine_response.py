from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_encryption_configuration import StepFunctionsEncryptionConfiguration
from .step_functions_logging_configuration import StepFunctionsLoggingConfiguration
from .step_functions_tracing_configuration import StepFunctionsTracingConfiguration


class StepFunctionsDescribeStateMachineResponse(BaseModel):
    stateMachineArn: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    definition: StrictStr | None = None
    roleArn: StrictStr | None = None
    type: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    loggingConfiguration: StepFunctionsLoggingConfiguration | None = None
    tracingConfiguration: StepFunctionsTracingConfiguration | None = None
    label: StrictStr | None = None
    revisionId: StrictStr | None = None
    description: StrictStr | None = None
    encryptionConfiguration: StepFunctionsEncryptionConfiguration | None = None
    variableReferences: dict[StrictStr, list[StrictStr]] | None = None
    ResponseMetadata: dict[str, Any] | None = None
