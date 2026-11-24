from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightPutPolicyAssignmentResponse(BaseModel):
    PolicyArn: StrictStr | None = None
    ReplacedPolicyArn: StrictStr | None = None
    Revision: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
