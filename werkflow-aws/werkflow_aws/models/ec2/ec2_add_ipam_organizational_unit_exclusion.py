from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AddIpamOrganizationalUnitExclusion(BaseModel):
    OrganizationsEntityPath: StrictStr | None = None
