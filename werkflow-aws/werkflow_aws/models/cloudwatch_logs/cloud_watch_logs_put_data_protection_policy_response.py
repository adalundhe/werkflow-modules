from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsPutDataProtectionPolicyResponse(BaseModel):
    logGroupIdentifier: StrictStr | None = None
    policyDocument: StrictStr | None = None
    lastUpdatedTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
