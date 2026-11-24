from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaChainedInvokeOptions(BaseModel):
    FunctionName: StrictStr
    TenantId: StrictStr | None = None
    XAmznTraceId: StrictStr | None = None
