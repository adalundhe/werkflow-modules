from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerRestoreSecretRequest(BaseModel):
    SecretId: StrictStr
