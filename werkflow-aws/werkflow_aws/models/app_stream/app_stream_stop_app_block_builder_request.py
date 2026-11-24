from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStopAppBlockBuilderRequest(BaseModel):
    Name: StrictStr
