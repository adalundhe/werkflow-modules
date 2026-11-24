from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DynamoDBGetResourcePolicyResponse(BaseModel):
    Policy: StrictStr | None = None
    RevisionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
