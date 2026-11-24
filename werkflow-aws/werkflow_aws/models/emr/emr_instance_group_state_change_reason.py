from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRInstanceGroupStateChangeReason(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
