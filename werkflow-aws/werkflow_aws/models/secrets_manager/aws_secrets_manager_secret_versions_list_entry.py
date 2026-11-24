from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerSecretVersionsListEntry(BaseModel):
    VersionId: StrictStr | None = None
    VersionStages: list[StrictStr] | None = None
    LastAccessedDate: datetime.datetime | StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    KmsKeyIds: list[StrictStr] | None = None
