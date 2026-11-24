from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaPauseDurableExecutionRequest(BaseModel):
    DurableExecutionArn: StrictStr
    ClientToken: StrictStr | None = None
    Reason: StrictStr | None = None
    ExecutionTimeoutPaused: StrictBool | None = None
