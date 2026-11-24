from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationCreateStackRefactorResponse(BaseModel):
    StackRefactorId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
