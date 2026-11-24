from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerUpdateClusterExtensionResponse(BaseModel):
    ExtensionArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
