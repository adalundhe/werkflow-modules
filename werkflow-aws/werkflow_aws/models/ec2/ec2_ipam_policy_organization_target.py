from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamPolicyOrganizationTarget(BaseModel):
    OrganizationTargetId: StrictStr | None = None
