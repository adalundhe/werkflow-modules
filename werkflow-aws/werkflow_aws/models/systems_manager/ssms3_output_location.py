from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMS3OutputLocation(BaseModel):
    OutputS3Region: StrictStr | None = None
    OutputS3BucketName: StrictStr | None = None
    OutputS3KeyPrefix: StrictStr | None = None
