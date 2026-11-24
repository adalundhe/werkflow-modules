from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListPoliciesRequest(BaseModel):
    marker: StrictStr | None = None
    pageSize: StrictInt | None = None
    ascendingOrder: StrictBool | None = None
