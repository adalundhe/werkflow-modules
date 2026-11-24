from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteResourcePolicyStatementResponse(BaseModel):
    resourceArn: StrictStr | None = None
    revisionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
