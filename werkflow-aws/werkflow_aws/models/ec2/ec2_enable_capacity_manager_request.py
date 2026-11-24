from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableCapacityManagerRequest(BaseModel):
    OrganizationsAccess: StrictBool | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
