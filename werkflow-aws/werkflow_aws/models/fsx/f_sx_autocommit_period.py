from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxAutocommitPeriod(BaseModel):
    Type: StrictStr | None = None
    Value: StrictInt | None = None
