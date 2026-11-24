from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointEventItemResponse(BaseModel):
    Message: StrictStr | None = None
    StatusCode: StrictInt | None = None
