from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationAttachmentFilter(BaseModel):
    Name: Literal['attachment-status']
    Values: list[StrictStr]
