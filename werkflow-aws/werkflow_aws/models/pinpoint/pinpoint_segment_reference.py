from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointSegmentReference(BaseModel):
    Id: StrictStr | None = None
    Version: StrictInt | None = None
