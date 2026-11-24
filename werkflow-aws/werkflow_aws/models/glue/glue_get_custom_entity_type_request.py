from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetCustomEntityTypeRequest(BaseModel):
    Name: StrictStr
