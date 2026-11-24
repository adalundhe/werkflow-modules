from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53AlarmIdentifierModel(BaseModel):
    Region: StrictStr | None = None
    Name: StrictStr | None = None
