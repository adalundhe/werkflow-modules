from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubIpOrganizationDetails(BaseModel):
    Asn: StrictInt | None = None
    AsnOrg: StrictStr | None = None
    Isp: StrictStr | None = None
    Org: StrictStr | None = None
