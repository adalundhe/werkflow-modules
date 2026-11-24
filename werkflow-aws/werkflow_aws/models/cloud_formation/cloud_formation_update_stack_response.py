from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationUpdateStackResponse(BaseModel):
    StackId: StrictStr | None = None
    OperationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
