from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteDataModelS3Configuration(BaseModel):
    BucketName: StrictStr | None = None
    ObjectKey: StrictStr | None = None
