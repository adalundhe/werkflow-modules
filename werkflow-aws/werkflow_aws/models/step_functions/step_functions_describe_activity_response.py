from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_encryption_configuration import StepFunctionsEncryptionConfiguration


class StepFunctionsDescribeActivityResponse(BaseModel):
    activityArn: StrictStr | None = None
    name: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    encryptionConfiguration: StepFunctionsEncryptionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
