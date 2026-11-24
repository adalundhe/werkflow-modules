from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceFamilyCreditSpecification(BaseModel):
    InstanceFamily: StrictStr | None = None
    CpuCredits: StrictStr | None = None
