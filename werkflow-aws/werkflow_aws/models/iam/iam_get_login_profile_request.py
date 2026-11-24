from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetLoginProfileRequest(BaseModel):
    UserName: StrictStr | None = None
