from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncS3ManifestConfig(BaseModel):
    ManifestObjectPath: StrictStr | None = None
    BucketAccessRoleArn: StrictStr | None = None
    S3BucketArn: StrictStr | None = None
    ManifestObjectVersionId: StrictStr | None = None
