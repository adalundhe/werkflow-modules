from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ExportToS3Task(BaseModel):
    ContainerFormat: StrictStr | None = None
    DiskImageFormat: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
