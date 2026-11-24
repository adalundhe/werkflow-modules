from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class OpenSearchUpdatePackageScopeRequest(BaseModel):
    PackageID: StrictStr
    Operation: Literal['ADD', 'OVERRIDE', 'REMOVE']
    PackageUserList: list[StrictStr]
