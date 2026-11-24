from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightS3BucketConfiguration(BaseModel):
    BucketName: StrictStr | None = None
    BucketPrefix: StrictStr | None = None
    BucketRegion: StrictStr | None = None
