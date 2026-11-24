from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMResourceRecord(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Value: StrictStr | None = None
