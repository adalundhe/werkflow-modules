from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTS3Location(BaseModel):
    bucket: StrictStr | None = None
    key: StrictStr | None = None
    version: StrictStr | None = None
