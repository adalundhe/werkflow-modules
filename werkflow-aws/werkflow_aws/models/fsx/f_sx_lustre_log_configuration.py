from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxLustreLogConfiguration(BaseModel):
    Level: StrictStr | None = None
    Destination: StrictStr | None = None
