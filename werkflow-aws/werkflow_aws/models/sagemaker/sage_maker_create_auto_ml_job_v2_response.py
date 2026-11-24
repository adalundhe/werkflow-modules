from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateAutoMLJobV2Response(BaseModel):
    AutoMLJobArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
