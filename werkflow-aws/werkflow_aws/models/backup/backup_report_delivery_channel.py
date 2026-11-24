from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupReportDeliveryChannel(BaseModel):
    S3BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    Formats: list[StrictStr] | None = None
