from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteDurableExecutionRequest(BaseModel):
    DurableExecutionArn: StrictStr
