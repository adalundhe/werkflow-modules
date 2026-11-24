from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneFailureCause(BaseModel):
    message: StrictStr | None = None
