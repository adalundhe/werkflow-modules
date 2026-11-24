from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRClusterStateChangeReason(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
