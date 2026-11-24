from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .step_functions_encryption_configuration import StepFunctionsEncryptionConfiguration
from .step_functions_tag import StepFunctionsTag


class StepFunctionsCreateActivityRequest(BaseModel):
    name: StrictStr
    tags: list[StepFunctionsTag] | None = None
    encryptionConfiguration: StepFunctionsEncryptionConfiguration | None = None
