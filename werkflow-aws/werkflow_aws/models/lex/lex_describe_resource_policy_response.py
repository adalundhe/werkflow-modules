from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDescribeResourcePolicyResponse(BaseModel):
    resourceArn: StrictStr | None = None
    policy: StrictStr | None = None
    revisionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
