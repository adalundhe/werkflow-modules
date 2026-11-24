from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaDeleteFunctionResponse(BaseModel):
    StatusCode: StrictInt | None = None
