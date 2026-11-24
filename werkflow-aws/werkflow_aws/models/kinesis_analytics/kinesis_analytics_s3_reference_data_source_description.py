from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ReferenceDataSourceDescription(BaseModel):
    BucketARN: StrictStr | None = None
    FileKey: StrictStr | None = None
    ReferenceRoleARN: StrictStr | None = None
