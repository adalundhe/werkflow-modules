from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MacieBucketPolicy(BaseModel):
    allowsPublicReadAccess: StrictBool | None = None
    allowsPublicWriteAccess: StrictBool | None = None
