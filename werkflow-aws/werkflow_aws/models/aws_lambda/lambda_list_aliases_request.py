from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListAliasesRequest(BaseModel):
    FunctionName: StrictStr
    FunctionVersion: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
