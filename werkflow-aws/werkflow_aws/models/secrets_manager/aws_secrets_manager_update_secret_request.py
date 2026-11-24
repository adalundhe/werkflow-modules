from __future__ import annotations
from pydantic import BaseModel, StrictBytes, StrictStr


class AWSSecretsManagerUpdateSecretRequest(BaseModel):
    SecretId: StrictStr
    ClientRequestToken: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    SecretBinary: StrictBytes | None = None
    SecretString: StrictStr | None = None
