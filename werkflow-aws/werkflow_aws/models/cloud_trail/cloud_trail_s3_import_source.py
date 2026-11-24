from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailS3ImportSource(BaseModel):
    S3LocationUri: StrictStr | None = None
    S3BucketRegion: StrictStr | None = None
    S3BucketAccessRoleArn: StrictStr | None = None
