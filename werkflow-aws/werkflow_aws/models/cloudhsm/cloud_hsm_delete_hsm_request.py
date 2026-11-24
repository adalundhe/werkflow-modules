from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMDeleteHsmRequest(BaseModel):
    ClusterId: StrictStr
    HsmId: StrictStr | None = None
    EniId: StrictStr | None = None
    EniIp: StrictStr | None = None
