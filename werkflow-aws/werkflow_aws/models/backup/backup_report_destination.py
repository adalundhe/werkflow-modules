from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupReportDestination(BaseModel):
    S3BucketName: StrictStr | None = None
    S3Keys: list[StrictStr] | None = None
