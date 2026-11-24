from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneTimezone(BaseModel):
    TimezoneName: StrictStr | None = None
