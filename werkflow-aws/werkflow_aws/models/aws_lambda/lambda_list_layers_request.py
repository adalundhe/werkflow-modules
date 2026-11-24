from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_architecture import LambdaArchitecture
from .lambda_runtime import LambdaRuntime


class LambdaListLayersRequest(BaseModel):
    CompatibleArchitecture: LambdaArchitecture | None = None
    CompatibleRuntime: LambdaRuntime | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
