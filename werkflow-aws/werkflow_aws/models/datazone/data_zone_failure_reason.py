from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneFailureReason(BaseModel):
    id: StrictStr | None = None
    message: StrictStr | None = None
