from __future__ import annotations
from pydantic import BaseModel, StrictBytes, StrictStr


class AWSSecretsManagerPutSecretValueRequest(BaseModel):
    SecretId: StrictStr
    ClientRequestToken: StrictStr | None = None
    SecretBinary: StrictBytes | None = None
    SecretString: StrictStr | None = None
    VersionStages: list[StrictStr] | None = None
    RotationToken: StrictStr | None = None
