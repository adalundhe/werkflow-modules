from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_account_level_permissions import GuardDutyAccountLevelPermissions
from .guard_duty_bucket_level_permissions import GuardDutyBucketLevelPermissions


class GuardDutyPermissionConfiguration(BaseModel):
    BucketLevelPermissions: GuardDutyBucketLevelPermissions | None = None
    AccountLevelPermissions: GuardDutyAccountLevelPermissions | None = None
