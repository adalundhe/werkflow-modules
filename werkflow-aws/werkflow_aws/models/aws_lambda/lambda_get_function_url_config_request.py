from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionUrlConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
