from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteOptedOutNumberRequest(BaseModel):
    OptOutListName: StrictStr
    OptedOutNumber: StrictStr
