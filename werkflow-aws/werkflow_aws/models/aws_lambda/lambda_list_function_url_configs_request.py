from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListFunctionUrlConfigsRequest(BaseModel):
    FunctionName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
