from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DNSSECStatus(BaseModel):
    ServeSignature: StrictStr | None = None
    StatusMessage: StrictStr | None = None
