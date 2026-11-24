from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetAliasRequest(BaseModel):
    FunctionName: StrictStr
    Name: StrictStr
