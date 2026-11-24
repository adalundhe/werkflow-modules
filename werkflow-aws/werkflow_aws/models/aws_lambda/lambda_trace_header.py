from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaTraceHeader(BaseModel):
    XAmznTraceId: StrictStr | None = None
