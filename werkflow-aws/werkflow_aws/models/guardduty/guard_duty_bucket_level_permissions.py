from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_access_control_list import GuardDutyAccessControlList
from .guard_duty_block_public_access import GuardDutyBlockPublicAccess
from .guard_duty_bucket_policy import GuardDutyBucketPolicy


class GuardDutyBucketLevelPermissions(BaseModel):
    AccessControlList: GuardDutyAccessControlList | None = None
    BucketPolicy: GuardDutyBucketPolicy | None = None
    BlockPublicAccess: GuardDutyBlockPublicAccess | None = None
