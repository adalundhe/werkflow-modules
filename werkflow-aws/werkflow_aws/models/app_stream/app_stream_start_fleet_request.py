from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStartFleetRequest(BaseModel):
    Name: StrictStr
