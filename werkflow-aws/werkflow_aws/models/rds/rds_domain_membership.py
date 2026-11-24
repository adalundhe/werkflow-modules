from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDomainMembership(BaseModel):
    Domain: StrictStr | None = None
    Status: StrictStr | None = None
    FQDN: StrictStr | None = None
    IAMRoleName: StrictStr | None = None
    OU: StrictStr | None = None
    AuthSecretArn: StrictStr | None = None
    DnsIps: list[StrictStr] | None = None
