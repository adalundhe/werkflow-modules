from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaFunctionRuntimeConfig(BaseModel):
    RuntimeArn: StrictStr
    RuntimeAlias: StrictStr
