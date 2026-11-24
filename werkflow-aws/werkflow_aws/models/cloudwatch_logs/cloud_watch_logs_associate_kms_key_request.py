from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsAssociateKmsKeyRequest(BaseModel):
    kmsKeyId: StrictStr
    logGroupName: StrictStr | None = None
    resourceIdentifier: StrictStr | None = None
