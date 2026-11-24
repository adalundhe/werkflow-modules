from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsEncryptionConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None
    kmsDataKeyReusePeriodSeconds: StrictInt | None = None
    type: StrictStr | None = None
