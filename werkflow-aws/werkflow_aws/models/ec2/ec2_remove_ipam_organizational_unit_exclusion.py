from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RemoveIpamOrganizationalUnitExclusion(BaseModel):
    OrganizationsEntityPath: StrictStr | None = None
