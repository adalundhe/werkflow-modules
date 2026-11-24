from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetContactListRequest(BaseModel):
    ContactListName: StrictStr
