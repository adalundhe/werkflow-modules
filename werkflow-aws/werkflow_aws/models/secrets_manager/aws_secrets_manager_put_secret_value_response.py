from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerPutSecretValueResponse(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    VersionId: StrictStr | None = None
    VersionStages: list[StrictStr] | None = None
