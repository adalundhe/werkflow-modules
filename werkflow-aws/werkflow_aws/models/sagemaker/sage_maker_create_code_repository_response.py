from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateCodeRepositoryResponse(BaseModel):
    CodeRepositoryArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
