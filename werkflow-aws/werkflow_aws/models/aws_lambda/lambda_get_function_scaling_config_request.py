from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionScalingConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr
