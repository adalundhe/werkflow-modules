from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionRecursionConfigRequest(BaseModel):
    FunctionName: StrictStr
