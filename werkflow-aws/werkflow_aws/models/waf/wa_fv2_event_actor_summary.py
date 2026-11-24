from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2EventActorSummary(BaseModel):
    EventActorId: StrictStr | None = None
    ClientIp: StrictStr | None = None
    TlsFingerprint: StrictStr | None = None
    Asn: StrictStr | None = None
    AsnOrganization: StrictStr | None = None
    Country: StrictStr | None = None
    AuthFingerprint: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    EventCount: StrictInt | None = None
