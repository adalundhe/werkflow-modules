from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WAFv2EventActorChange(BaseModel):
    ChangeTime: datetime.datetime | StrictStr | None = None
    ClientIp: StrictStr | None = None
    TlsFingerprint: StrictStr | None = None
    Asn: StrictStr | None = None
    AsnOrganization: StrictStr | None = None
    Country: StrictStr | None = None
