from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsS3AccountPublicAccessBlockDetails(BaseModel):
    BlockPublicAcls: StrictBool | None = None
    BlockPublicPolicy: StrictBool | None = None
    IgnorePublicAcls: StrictBool | None = None
    RestrictPublicBuckets: StrictBool | None = None
