from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaGetProvisionedConcurrencyConfigResponse(BaseModel):
    RequestedProvisionedConcurrentExecutions: StrictInt | None = None
    AvailableProvisionedConcurrentExecutions: StrictInt | None = None
    AllocatedProvisionedConcurrentExecutions: StrictInt | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    LastModified: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
