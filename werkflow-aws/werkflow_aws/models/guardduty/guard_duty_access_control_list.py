from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyAccessControlList(BaseModel):
    AllowsPublicReadAccess: StrictBool | None = None
    AllowsPublicWriteAccess: StrictBool | None = None
