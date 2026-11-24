from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LambdaPutFunctionRecursionConfigRequest(BaseModel):
    FunctionName: StrictStr
    RecursiveLoop: Literal['Allow', 'Terminate']
