from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateJsonClassifierRequest(BaseModel):
    Name: StrictStr
    JsonPath: StrictStr | None = None
