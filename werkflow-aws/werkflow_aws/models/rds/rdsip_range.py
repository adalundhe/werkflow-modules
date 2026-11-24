from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSIPRange(BaseModel):
    Status: StrictStr | None = None
    CIDRIP: StrictStr | None = None
