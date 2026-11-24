from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointSimpleEmailPart(BaseModel):
    Charset: StrictStr | None = None
    Data: StrictStr | None = None
