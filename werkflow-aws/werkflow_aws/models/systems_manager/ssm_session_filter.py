from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMSessionFilter(BaseModel):
    key: Literal['InvokedAfter', 'InvokedBefore', 'Target', 'Owner', 'Status', 'SessionId', 'AccessType']
    value: StrictStr
