from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_cors import LambdaCors


class LambdaUpdateFunctionUrlConfigResponse(BaseModel):
    FunctionUrl: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    AuthType: StrictStr | None = None
    Cors: LambdaCors | None = None
    CreationTime: StrictStr | None = None
    LastModifiedTime: StrictStr | None = None
    InvokeMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
