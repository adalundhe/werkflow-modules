from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from typing import Literal


class AWSSecretsManagerReplicationStatus(BaseModel):
    Region: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Status: Literal['InSync', 'Failed', 'InProgress'] | None = None
    StatusMessage: StrictStr | None = None
    LastAccessedDate: datetime.datetime | None = None
