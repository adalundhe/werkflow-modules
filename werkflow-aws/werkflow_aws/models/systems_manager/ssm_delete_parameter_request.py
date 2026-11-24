from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteParameterRequest(BaseModel):
    Name: StrictStr
