from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteCustomEntityTypeRequest(BaseModel):
    Name: StrictStr
