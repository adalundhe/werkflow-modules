from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteParametersRequest(BaseModel):
    Names: list[StrictStr]
