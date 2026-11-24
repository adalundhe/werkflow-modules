from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSSCApplicationAttributes(BaseModel):
    S3BucketPath: StrictStr | None = None
    S3BucketRoleArn: StrictStr | None = None
