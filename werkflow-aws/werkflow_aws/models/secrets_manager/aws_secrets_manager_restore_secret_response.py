from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerRestoreSecretResponse(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
