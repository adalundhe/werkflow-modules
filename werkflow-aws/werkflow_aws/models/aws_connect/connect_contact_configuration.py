from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectContactConfiguration(BaseModel):
    ContactId: StrictStr
    ParticipantRole: Literal['AGENT', 'CUSTOMER', 'SYSTEM', 'CUSTOM_BOT', 'SUPERVISOR'] | None = None
    IncludeRawMessage: StrictBool | None = None
