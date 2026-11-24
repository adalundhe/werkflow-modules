from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteAccessKeyRequest(BaseModel):
    AccessKeyId: StrictStr
    UserName: StrictStr | None = None
