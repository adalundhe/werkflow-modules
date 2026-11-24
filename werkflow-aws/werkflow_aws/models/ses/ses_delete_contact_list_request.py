from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteContactListRequest(BaseModel):
    ContactListName: StrictStr
