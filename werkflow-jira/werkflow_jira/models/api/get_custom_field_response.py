from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class GetCustomFieldResponse(BaseModel):
    customFieldId: StrictInt | None = None
    filter: StrictBool | None = None
