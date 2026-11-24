from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ResourceRecord(BaseModel):
    Value: StrictStr | None = None
