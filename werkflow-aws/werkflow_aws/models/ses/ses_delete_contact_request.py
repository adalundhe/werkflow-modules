from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteContactRequest(BaseModel):
    ContactListName: StrictStr
    EmailAddress: StrictStr
