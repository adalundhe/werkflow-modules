from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceCreditSpecificationRequest(BaseModel):
    InstanceId: StrictStr
    CpuCredits: StrictStr | None = None
