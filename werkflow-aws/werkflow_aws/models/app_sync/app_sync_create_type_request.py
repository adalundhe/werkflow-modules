from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppSyncCreateTypeRequest(BaseModel):
    apiId: StrictStr
    definition: StrictStr
    format: Literal['SDL', 'JSON']
