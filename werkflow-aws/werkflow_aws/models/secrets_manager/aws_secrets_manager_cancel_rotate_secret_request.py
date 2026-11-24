from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerCancelRotateSecretRequest(BaseModel):
    SecretId: StrictStr
