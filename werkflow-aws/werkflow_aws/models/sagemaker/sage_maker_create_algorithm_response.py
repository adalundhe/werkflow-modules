from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateAlgorithmResponse(BaseModel):
    AlgorithmArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
