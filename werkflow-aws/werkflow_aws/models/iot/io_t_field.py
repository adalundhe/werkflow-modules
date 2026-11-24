from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTField(BaseModel):
    name: StrictStr | None = None
    type: StrictStr | None = None
