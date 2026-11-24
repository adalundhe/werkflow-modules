from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteFunctionConcurrencyRequest(BaseModel):
    FunctionName: StrictStr
