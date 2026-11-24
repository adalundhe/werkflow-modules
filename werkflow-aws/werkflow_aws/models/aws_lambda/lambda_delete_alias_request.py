from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteAliasRequest(BaseModel):
    FunctionName: StrictStr
    Name: StrictStr
