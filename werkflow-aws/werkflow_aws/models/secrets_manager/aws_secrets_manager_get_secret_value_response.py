import datetime
from pydantic import BaseModel, StrictStr, StrictBytes


class AWSSecretManagerGetSecretValueResponse(BaseModel):
    ARN: StrictStr
    Name: StrictStr
    VersionId: StrictStr | None = None
    SecretBinary: StrictBytes
    SecretString: StrictStr
    VersionStages: list[StrictStr] | None = None
    CreatedDate: datetime.datetime
