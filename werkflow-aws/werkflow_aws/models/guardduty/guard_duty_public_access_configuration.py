from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyPublicAccessConfiguration(BaseModel):
    PublicAclAccess: StrictStr | None = None
    PublicPolicyAccess: StrictStr | None = None
    PublicAclIgnoreBehavior: StrictStr | None = None
    PublicBucketRestrictBehavior: StrictStr | None = None
