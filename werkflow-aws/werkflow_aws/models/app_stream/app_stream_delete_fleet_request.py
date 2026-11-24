from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteFleetRequest(BaseModel):
    Name: StrictStr
