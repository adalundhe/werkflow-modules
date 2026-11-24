from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyBlockPublicAccess(BaseModel):
    IgnorePublicAcls: StrictBool | None = None
    RestrictPublicBuckets: StrictBool | None = None
    BlockPublicAcls: StrictBool | None = None
    BlockPublicPolicy: StrictBool | None = None
