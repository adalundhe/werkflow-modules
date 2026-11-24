from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaPutFunctionConcurrencyRequest(BaseModel):
    FunctionName: StrictStr
    ReservedConcurrentExecutions: StrictInt
