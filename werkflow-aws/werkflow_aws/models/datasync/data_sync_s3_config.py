from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncS3Config(BaseModel):
    BucketAccessRoleArn: StrictStr | None = None
