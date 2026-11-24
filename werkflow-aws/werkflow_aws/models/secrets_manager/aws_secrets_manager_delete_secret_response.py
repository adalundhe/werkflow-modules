from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerDeleteSecretResponse(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    DeletionDate: datetime.datetime | None = None
