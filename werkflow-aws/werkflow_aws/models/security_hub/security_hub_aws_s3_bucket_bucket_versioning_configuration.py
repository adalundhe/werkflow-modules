from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsS3BucketBucketVersioningConfiguration(BaseModel):
    IsMfaDeleteEnabled: StrictBool | None = None
    Status: StrictStr | None = None
