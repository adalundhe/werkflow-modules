from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMGetParametersRequest(BaseModel):
    Names: list[StrictStr]
    WithDecryption: StrictBool | None = None
