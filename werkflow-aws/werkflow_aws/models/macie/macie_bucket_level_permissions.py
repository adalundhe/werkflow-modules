from __future__ import annotations
from pydantic import BaseModel
from .macie_access_control_list import MacieAccessControlList
from .macie_block_public_access import MacieBlockPublicAccess
from .macie_bucket_policy import MacieBucketPolicy


class MacieBucketLevelPermissions(BaseModel):
    accessControlList: MacieAccessControlList | None = None
    blockPublicAccess: MacieBlockPublicAccess | None = None
    bucketPolicy: MacieBucketPolicy | None = None
