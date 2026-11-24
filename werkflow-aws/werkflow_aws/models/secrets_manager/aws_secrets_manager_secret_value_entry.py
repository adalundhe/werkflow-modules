from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class AWSSecretsManagerSecretValueEntry(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    VersionId: StrictStr | None = None
    SecretBinary: StrictBytes | Any | None = None
    SecretString: StrictStr | None = None
    VersionStages: list[StrictStr] | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
