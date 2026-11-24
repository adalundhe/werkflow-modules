from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSHostEntry(BaseModel):
    hostname: StrictStr | None = None
    ipAddress: StrictStr | None = None
