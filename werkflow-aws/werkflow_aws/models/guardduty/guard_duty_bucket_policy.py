from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyBucketPolicy(BaseModel):
    AllowsPublicReadAccess: StrictBool | None = None
    AllowsPublicWriteAccess: StrictBool | None = None
