from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTHttpActionHeader(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
