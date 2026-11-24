from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamCreateAppBlockBuilderStreamingURLRequest(BaseModel):
    AppBlockBuilderName: StrictStr
    Validity: StrictInt | None = None
