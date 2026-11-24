from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PtrUpdateStatus(BaseModel):
    Value: StrictStr | None = None
    Status: StrictStr | None = None
    Reason: StrictStr | None = None
