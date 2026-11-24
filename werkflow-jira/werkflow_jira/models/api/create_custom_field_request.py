from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class CreateCustomFieldRequest(BaseModel):
    customFieldId: StrictInt | None = None
    filter: StrictBool | None = None
