from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyOrganization(BaseModel):
    Asn: StrictStr | None = None
    AsnOrg: StrictStr | None = None
    Isp: StrictStr | None = None
    Org: StrictStr | None = None
