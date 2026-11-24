from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteLoginProfileRequest(BaseModel):
    UserName: StrictStr | None = None
