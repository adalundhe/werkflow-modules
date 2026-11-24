from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetClassifierRequest(BaseModel):
    Name: StrictStr
