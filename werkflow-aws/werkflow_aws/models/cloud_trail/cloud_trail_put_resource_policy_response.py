from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailPutResourcePolicyResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    ResourcePolicy: StrictStr | None = None
    DelegatedAdminResourcePolicy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
