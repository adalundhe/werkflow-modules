from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingSetDefaultMessageTypeRequest(BaseModel):
    ConfigurationSetName: StrictStr
    MessageType: Literal['TRANSACTIONAL', 'PROMOTIONAL']
