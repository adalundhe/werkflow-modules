from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class BatchDescribeConsumableResourceResponse(BaseModel):
    consumableResourceName: StrictStr | None = None
    consumableResourceArn: StrictStr | None = None
    totalQuantity: StrictInt | None = None
    inUseQuantity: StrictInt | None = None
    availableQuantity: StrictInt | None = None
    resourceType: StrictStr | None = None
    createdAt: StrictInt | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
