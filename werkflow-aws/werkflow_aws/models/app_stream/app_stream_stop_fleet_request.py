from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStopFleetRequest(BaseModel):
    Name: StrictStr
