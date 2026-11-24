from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppSyncGetTypeRequest(BaseModel):
    apiId: StrictStr
    typeName: StrictStr
    format: Literal['SDL', 'JSON']
