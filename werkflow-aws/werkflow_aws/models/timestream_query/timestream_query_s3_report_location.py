from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryS3ReportLocation(BaseModel):
    BucketName: StrictStr | None = None
    ObjectKey: StrictStr | None = None
