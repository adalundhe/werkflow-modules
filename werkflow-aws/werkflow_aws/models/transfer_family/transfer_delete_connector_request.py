from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteConnectorRequest(BaseModel):
    ConnectorId: StrictStr
