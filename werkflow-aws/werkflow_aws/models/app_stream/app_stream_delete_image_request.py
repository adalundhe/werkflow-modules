from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteImageRequest(BaseModel):
    Name: StrictStr
