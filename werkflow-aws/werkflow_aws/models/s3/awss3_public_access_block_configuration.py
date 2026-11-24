from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AWSS3PublicAccessBlockConfiguration(BaseModel):
    BlockPublicAcls: StrictBool | None = None
    IgnorePublicAcls: StrictBool | None = None
    BlockPublicPolicy: StrictBool | None = None
    RestrictPublicBuckets: StrictBool | None = None
