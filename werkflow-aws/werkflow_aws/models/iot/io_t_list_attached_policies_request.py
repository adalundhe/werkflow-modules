from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListAttachedPoliciesRequest(BaseModel):
    target: StrictStr
    recursive: StrictBool | None = None
    marker: StrictStr | None = None
    pageSize: StrictInt | None = None
