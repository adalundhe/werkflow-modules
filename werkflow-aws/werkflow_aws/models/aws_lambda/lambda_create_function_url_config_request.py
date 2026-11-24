from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lambda_cors import LambdaCors


class LambdaCreateFunctionUrlConfigRequest(BaseModel):
    FunctionName: StrictStr
    AuthType: Literal['NONE', 'AWS_IAM']
    Qualifier: StrictStr | None = None
    Cors: LambdaCors | None = None
    InvokeMode: Literal['BUFFERED', 'RESPONSE_STREAM'] | None = None
