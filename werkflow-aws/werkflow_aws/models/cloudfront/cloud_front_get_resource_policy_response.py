from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFrontGetResourcePolicyResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
