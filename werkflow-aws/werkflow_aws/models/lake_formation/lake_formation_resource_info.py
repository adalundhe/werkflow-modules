from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class LakeFormationResourceInfo(BaseModel):
    ResourceArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    WithFederation: StrictBool | None = None
    HybridAccessEnabled: StrictBool | None = None
    WithPrivilegedAccess: StrictBool | None = None
    VerificationStatus: StrictStr | None = None
    ExpectedResourceOwnerAccount: StrictStr | None = None
