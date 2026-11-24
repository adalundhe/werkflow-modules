from __future__ import annotations
from pydantic import BaseModel
from .macie_account_level_permissions import MacieAccountLevelPermissions
from .macie_bucket_level_permissions import MacieBucketLevelPermissions


class MacieBucketPermissionConfiguration(BaseModel):
    accountLevelPermissions: MacieAccountLevelPermissions | None = None
    bucketLevelPermissions: MacieBucketLevelPermissions | None = None
