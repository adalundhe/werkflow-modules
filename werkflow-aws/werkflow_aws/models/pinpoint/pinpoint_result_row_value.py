from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointResultRowValue(BaseModel):
    Key: StrictStr | None = None
    Type: StrictStr | None = None
    Value: StrictStr | None = None
