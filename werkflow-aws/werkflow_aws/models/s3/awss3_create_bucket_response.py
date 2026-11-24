from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3CreateBucketResponse(BaseModel):
    Location: StrictStr | None = None
    BucketArn: StrictStr | None = None
