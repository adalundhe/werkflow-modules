from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetPolicyRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
