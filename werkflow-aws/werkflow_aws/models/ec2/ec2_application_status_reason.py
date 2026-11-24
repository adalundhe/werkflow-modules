from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ApplicationStatusReason(BaseModel):
    Code: StrictStr | None = None
    StatusCode: StrictInt | None = None
    Protocol: StrictStr | None = None
