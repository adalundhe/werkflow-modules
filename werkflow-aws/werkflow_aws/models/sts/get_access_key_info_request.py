from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GetAccessKeyInfoRequest(BaseModel):
    AccessKeyId: StrictStr | None = None
