from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2UnsuccessfulInstanceCreditSpecificationItemError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
