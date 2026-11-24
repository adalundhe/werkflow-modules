from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LambdaPutRuntimeManagementConfigRequest(BaseModel):
    FunctionName: StrictStr
    UpdateRuntimeOn: Literal['Auto', 'Manual', 'FunctionUpdate']
    Qualifier: StrictStr | None = None
    RuntimeVersionArn: StrictStr | None = None
