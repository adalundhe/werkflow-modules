from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaResumeDurableExecutionRequest(BaseModel):
    DurableExecutionArn: StrictStr
    ClientToken: StrictStr | None = None
    Reason: StrictStr | None = None
