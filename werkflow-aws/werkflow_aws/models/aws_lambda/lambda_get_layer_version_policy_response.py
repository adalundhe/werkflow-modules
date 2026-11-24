from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LambdaGetLayerVersionPolicyResponse(BaseModel):
    Policy: StrictStr | None = None
    RevisionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
