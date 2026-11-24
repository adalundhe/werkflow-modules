from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubS3ExportDestination(BaseModel):
    BucketArn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    ObjectPrefix: StrictStr | None = None
