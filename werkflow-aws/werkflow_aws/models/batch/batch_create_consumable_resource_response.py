from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchCreateConsumableResourceResponse(BaseModel):
    consumableResourceName: StrictStr | None = None
    consumableResourceArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
