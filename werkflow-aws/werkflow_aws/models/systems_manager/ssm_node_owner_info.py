from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMNodeOwnerInfo(BaseModel):
    AccountId: StrictStr | None = None
    OrganizationalUnitId: StrictStr | None = None
    OrganizationalUnitPath: StrictStr | None = None
