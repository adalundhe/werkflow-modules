from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMCreateAccessKeyRequest(BaseModel):
    UserName: StrictStr | None = None
