from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTTimeFilter(BaseModel):
    after: StrictStr | None = None
    before: StrictStr | None = None
