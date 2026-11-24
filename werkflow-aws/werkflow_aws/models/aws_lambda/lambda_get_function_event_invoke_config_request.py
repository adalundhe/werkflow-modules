from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionEventInvokeConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
