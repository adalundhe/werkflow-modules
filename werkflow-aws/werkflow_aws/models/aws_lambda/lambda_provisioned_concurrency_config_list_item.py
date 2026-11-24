from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaProvisionedConcurrencyConfigListItem(BaseModel):
    FunctionArn: StrictStr | None = None
    RequestedProvisionedConcurrentExecutions: StrictInt | None = None
    AvailableProvisionedConcurrentExecutions: StrictInt | None = None
    AllocatedProvisionedConcurrentExecutions: StrictInt | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    LastModified: StrictStr | None = None
