from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMGetParameterRequest(BaseModel):
    Name: StrictStr
    WithDecryption: StrictBool | None = None
