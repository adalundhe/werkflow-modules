from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VerifiedAccessLogS3DestinationOptions(BaseModel):
    Enabled: StrictBool
    BucketName: StrictStr | None = None
    Prefix: StrictStr | None = None
    BucketOwner: StrictStr | None = None
