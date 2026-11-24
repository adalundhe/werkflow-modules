from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationJobInputOptions(BaseModel):
    Location: StrictStr | None = None
    Format: StrictStr | None = None
