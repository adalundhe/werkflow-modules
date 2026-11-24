from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AWSS3HeadBucketResponse(BaseModel):
    BucketArn: StrictStr | None = None
    BucketLocationType: StrictStr | None = None
    BucketLocationName: StrictStr | None = None
    BucketRegion: StrictStr | None = None
    AccessPointAlias: StrictBool | None = None
