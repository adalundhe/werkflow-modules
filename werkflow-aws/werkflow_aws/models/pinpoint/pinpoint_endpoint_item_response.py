from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointEndpointItemResponse(BaseModel):
    Message: StrictStr | None = None
    StatusCode: StrictInt | None = None
