from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationJobError(BaseModel):
    Code: StrictStr | None = None
    Messages: list[StrictStr] | None = None
