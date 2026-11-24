from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CreditSpecification(BaseModel):
    CpuCredits: StrictStr | None = None
