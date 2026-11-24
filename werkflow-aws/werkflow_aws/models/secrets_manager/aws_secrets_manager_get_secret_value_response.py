import datetime
from pydantic import BaseModel, StrictBytes, StrictStr


class AWSSecretsManagerGetSecretValueResponse(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    VersionId: StrictStr | None = None
    SecretBinary: StrictBytes | None = None
    SecretString: StrictStr | None = None
    VersionStages: list[StrictStr] | None = None
    CreatedDate: datetime.datetime | None = None


AWSSecretManagerGetSecretValueResponse = AWSSecretsManagerGetSecretValueResponse
