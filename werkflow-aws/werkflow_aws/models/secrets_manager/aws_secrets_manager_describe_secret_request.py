from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerDescribeSecretRequest(BaseModel):
    SecretId: StrictStr
