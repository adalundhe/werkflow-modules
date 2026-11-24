from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointApplicationResponse(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    CreationDate: StrictStr | None = None
