from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .iam_access_key_last_used import IAMAccessKeyLastUsed


class IAMGetAccessKeyLastUsedResponse(BaseModel):
    UserName: StrictStr | None = None
    AccessKeyLastUsed: IAMAccessKeyLastUsed | None = None
    ResponseMetadata: dict[str, Any] | None = None
