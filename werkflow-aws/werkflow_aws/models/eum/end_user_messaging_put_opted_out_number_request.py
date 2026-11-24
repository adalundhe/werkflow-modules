from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutOptedOutNumberRequest(BaseModel):
    OptOutListName: StrictStr
    OptedOutNumber: StrictStr
