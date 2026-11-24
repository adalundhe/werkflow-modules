from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPolicyGrantingServiceAccess(BaseModel):
    PolicyName: StrictStr | None = None
    PolicyType: StrictStr | None = None
    PolicyArn: StrictStr | None = None
    EntityType: StrictStr | None = None
    EntityName: StrictStr | None = None
