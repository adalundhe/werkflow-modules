from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMLabelParameterVersionRequest(BaseModel):
    Name: StrictStr
    Labels: list[StrictStr]
    ParameterVersion: StrictInt | None = None
