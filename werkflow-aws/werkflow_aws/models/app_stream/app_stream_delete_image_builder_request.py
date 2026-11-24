from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteImageBuilderRequest(BaseModel):
    Name: StrictStr
