from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LaunchPermission(BaseModel):
    OrganizationArn: StrictStr | None = None
    OrganizationalUnitArn: StrictStr | None = None
    UserId: StrictStr | None = None
    Group: StrictStr | None = None
