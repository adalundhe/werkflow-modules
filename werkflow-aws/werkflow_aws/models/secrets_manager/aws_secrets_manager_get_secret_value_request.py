from pydantic import BaseModel, StrictStr


class AWSSecretsManagerGetSecretValueRequest(BaseModel):
    SecretId: StrictStr
    VersionId: StrictStr | None = None
    VersionStage: StrictStr | None = None
