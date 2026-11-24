from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_bucket_permission_configuration import MacieBucketPermissionConfiguration


class MacieBucketPublicAccess(BaseModel):
    effectivePermission: StrictStr | None = None
    permissionConfiguration: MacieBucketPermissionConfiguration | None = None
