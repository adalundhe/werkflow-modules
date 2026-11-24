from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListAuthorizersRequest(BaseModel):
    pageSize: StrictInt | None = None
    marker: StrictStr | None = None
    ascendingOrder: StrictBool | None = None
    status: Literal['ACTIVE', 'INACTIVE'] | None = None
