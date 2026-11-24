from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSCancelUpdateRequest(BaseModel):
    name: StrictStr
    updateId: StrictStr
    clientRequestToken: StrictStr | None = None
