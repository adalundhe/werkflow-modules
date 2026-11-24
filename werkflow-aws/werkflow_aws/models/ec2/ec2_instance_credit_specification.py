from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceCreditSpecification(BaseModel):
    InstanceId: StrictStr | None = None
    CpuCredits: StrictStr | None = None
