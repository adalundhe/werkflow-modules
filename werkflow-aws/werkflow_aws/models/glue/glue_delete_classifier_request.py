from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteClassifierRequest(BaseModel):
    Name: StrictStr
