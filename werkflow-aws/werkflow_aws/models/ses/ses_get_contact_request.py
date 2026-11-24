from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetContactRequest(BaseModel):
    ContactListName: StrictStr
    EmailAddress: StrictStr
