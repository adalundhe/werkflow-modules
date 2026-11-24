from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamOrganizationalUnitExclusion(BaseModel):
    OrganizationsEntityPath: StrictStr | None = None
