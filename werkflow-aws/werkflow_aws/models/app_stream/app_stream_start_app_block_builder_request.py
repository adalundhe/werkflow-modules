from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamStartAppBlockBuilderRequest(BaseModel):
    Name: StrictStr
