from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDeleteContextResponse(BaseModel):
    ContextArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
