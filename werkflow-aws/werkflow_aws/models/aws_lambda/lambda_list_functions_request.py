from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_function_version import LambdaFunctionVersion


class LambdaListFunctionsRequest(BaseModel):
    MasterRegion: StrictStr | None = None
    FunctionVersion: LambdaFunctionVersion | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
