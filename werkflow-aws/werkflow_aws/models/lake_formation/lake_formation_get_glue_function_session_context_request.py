from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationGetGlueFunctionSessionContextRequest(BaseModel):
    UserDefinedFunctionArns: list[StrictStr]
    DurationSeconds: StrictInt | None = None
