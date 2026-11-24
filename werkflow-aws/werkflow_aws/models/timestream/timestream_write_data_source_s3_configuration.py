from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteDataSourceS3Configuration(BaseModel):
    BucketName: StrictStr | None = None
    ObjectKeyPrefix: StrictStr | None = None
