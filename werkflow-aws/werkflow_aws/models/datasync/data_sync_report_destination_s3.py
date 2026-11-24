from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncReportDestinationS3(BaseModel):
    Subdirectory: StrictStr | None = None
    S3BucketArn: StrictStr | None = None
    BucketAccessRoleArn: StrictStr | None = None
