from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ResourceRecordModel(BaseModel):
    Value: StrictStr | None = None
