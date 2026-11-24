from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_cors import LambdaCors


class LambdaFunctionUrlConfig(BaseModel):
    FunctionUrl: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    CreationTime: StrictStr | None = None
    LastModifiedTime: StrictStr | None = None
    Cors: LambdaCors | None = None
    AuthType: StrictStr | None = None
    InvokeMode: StrictStr | None = None
