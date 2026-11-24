from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class BatchUpdateConsumableResourceResponse(BaseModel):
    consumableResourceName: StrictStr | None = None
    consumableResourceArn: StrictStr | None = None
    totalQuantity: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
