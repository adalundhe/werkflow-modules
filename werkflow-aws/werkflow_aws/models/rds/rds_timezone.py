from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSTimezone(BaseModel):
    TimezoneName: StrictStr | None = None
