from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamCreateImageBuilderStreamingURLRequest(BaseModel):
    Name: StrictStr
    Validity: StrictInt | None = None
