from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchCreateServiceEnvironmentResponse(BaseModel):
    serviceEnvironmentName: StrictStr | None = None
    serviceEnvironmentArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
