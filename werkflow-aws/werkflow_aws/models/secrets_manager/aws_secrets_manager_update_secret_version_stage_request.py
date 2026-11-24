from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerUpdateSecretVersionStageRequest(BaseModel):
    SecretId: StrictStr
    VersionStage: StrictStr
    RemoveFromVersionId: StrictStr | None = None
    MoveToVersionId: StrictStr | None = None
