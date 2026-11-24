from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDisassociateKmsKeyRequest(BaseModel):
    logGroupName: StrictStr | None = None
    resourceIdentifier: StrictStr | None = None
