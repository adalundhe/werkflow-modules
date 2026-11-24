from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionConcurrencyRequest(BaseModel):
    FunctionName: StrictStr
