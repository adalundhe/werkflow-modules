from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaGetDurableExecutionRequest(BaseModel):
    DurableExecutionArn: StrictStr
    IncludeExecutionData: StrictBool | None = None
