from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationJobOutputOptions(BaseModel):
    Format: StrictStr | None = None
    Location: StrictStr | None = None
