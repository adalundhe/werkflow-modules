from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteFunctionCodeSigningConfigRequest(BaseModel):
    FunctionName: StrictStr
