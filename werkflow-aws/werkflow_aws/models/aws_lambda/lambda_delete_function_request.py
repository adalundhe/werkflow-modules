from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteFunctionRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
