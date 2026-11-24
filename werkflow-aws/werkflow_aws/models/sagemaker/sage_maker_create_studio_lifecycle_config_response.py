from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateStudioLifecycleConfigResponse(BaseModel):
    StudioLifecycleConfigArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
