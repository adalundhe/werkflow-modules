from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetFunctionConfigurationRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
