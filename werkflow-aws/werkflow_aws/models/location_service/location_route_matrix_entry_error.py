from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationRouteMatrixEntryError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
