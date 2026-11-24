from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SuccessfulInstanceCreditSpecificationItem(BaseModel):
    InstanceId: StrictStr | None = None
