from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableIpamPolicyRequest(BaseModel):
    IpamPolicyId: StrictStr
    DryRun: StrictBool | None = None
    OrganizationTargetId: StrictStr | None = None
