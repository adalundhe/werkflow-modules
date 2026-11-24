from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTS3Destination(BaseModel):
    bucket: StrictStr | None = None
    prefix: StrictStr | None = None
