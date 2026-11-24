from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaPutFunctionCodeSigningConfigRequest(BaseModel):
    CodeSigningConfigArn: StrictStr
    FunctionName: StrictStr
