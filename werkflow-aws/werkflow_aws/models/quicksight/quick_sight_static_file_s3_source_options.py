from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStaticFileS3SourceOptions(BaseModel):
    BucketName: StrictStr | None = None
    ObjectKey: StrictStr | None = None
    Region: StrictStr | None = None
