from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMUnlabelParameterVersionRequest(BaseModel):
    Name: StrictStr
    ParameterVersion: StrictInt
    Labels: list[StrictStr]
