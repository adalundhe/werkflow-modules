from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lambda_cors import LambdaCors


class LambdaUpdateFunctionUrlConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
    AuthType: Literal['NONE', 'AWS_IAM'] | None = None
    Cors: LambdaCors | None = None
    InvokeMode: Literal['BUFFERED', 'RESPONSE_STREAM'] | None = None
