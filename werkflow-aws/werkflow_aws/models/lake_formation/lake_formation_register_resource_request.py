from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LakeFormationRegisterResourceRequest(BaseModel):
    ResourceArn: StrictStr
    UseServiceLinkedRole: StrictBool | None = None
    RoleArn: StrictStr | None = None
    WithFederation: StrictBool | None = None
    HybridAccessEnabled: StrictBool | None = None
    WithPrivilegedAccess: StrictBool | None = None
    ExpectedResourceOwnerAccount: StrictStr | None = None
