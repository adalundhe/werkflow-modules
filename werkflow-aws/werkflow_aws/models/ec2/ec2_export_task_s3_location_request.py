from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ExportTaskS3LocationRequest(BaseModel):
    S3Bucket: StrictStr
    S3Prefix: StrictStr | None = None
