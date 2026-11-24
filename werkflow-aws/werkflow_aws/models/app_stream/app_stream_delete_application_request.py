from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteApplicationRequest(BaseModel):
    Name: StrictStr
