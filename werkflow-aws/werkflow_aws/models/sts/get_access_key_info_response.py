from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GetAccessKeyInfoResponse(BaseModel):
    Account: StrictStr | None = None
