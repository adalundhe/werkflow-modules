from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsS3Configuration(BaseModel):
    destinationIdentifier: StrictStr | None = None
    roleArn: StrictStr | None = None
    ownerAccountId: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
