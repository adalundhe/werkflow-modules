from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_block_public_access import GuardDutyBlockPublicAccess


class GuardDutyAccountLevelPermissions(BaseModel):
    BlockPublicAccess: GuardDutyBlockPublicAccess | None = None
