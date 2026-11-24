from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateJsonClassifierRequest(BaseModel):
    Name: StrictStr
    JsonPath: StrictStr
