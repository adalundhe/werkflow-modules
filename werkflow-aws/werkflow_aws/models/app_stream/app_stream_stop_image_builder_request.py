from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStopImageBuilderRequest(BaseModel):
    Name: StrictStr
