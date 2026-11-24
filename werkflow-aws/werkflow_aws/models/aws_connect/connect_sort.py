from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectSort(BaseModel):
    FieldName: Literal['INITIATION_TIMESTAMP', 'SCHEDULED_TIMESTAMP', 'CONNECTED_TO_AGENT_TIMESTAMP', 'DISCONNECT_TIMESTAMP', 'INITIATION_METHOD', 'CHANNEL', 'EXPIRY_TIMESTAMP']
    Order: Literal['ASCENDING', 'DESCENDING']
