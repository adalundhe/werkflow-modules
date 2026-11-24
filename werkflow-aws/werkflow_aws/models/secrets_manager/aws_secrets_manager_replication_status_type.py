from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerReplicationStatusType(BaseModel):
    Region: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    LastAccessedDate: datetime.datetime | StrictStr | None = None
