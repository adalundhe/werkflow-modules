from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AWSSecretsManagerDeleteSecretRequest(BaseModel):
    SecretId: StrictStr
    RecoveryWindowInDays: StrictInt | None = None
    ForceDeleteWithoutRecovery: StrictBool | None = None
