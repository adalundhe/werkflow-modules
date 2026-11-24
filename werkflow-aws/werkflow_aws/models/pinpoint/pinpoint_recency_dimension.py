from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointRecencyDimension(BaseModel):
    Duration: StrictStr | None = None
    RecencyType: StrictStr | None = None
