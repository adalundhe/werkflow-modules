from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LakeFormationUpdateResourceRequest(BaseModel):
    RoleArn: StrictStr
    ResourceArn: StrictStr
    WithFederation: StrictBool | None = None
    HybridAccessEnabled: StrictBool | None = None
    ExpectedResourceOwnerAccount: StrictStr | None = None
