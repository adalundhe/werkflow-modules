from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeConnectorRequest(BaseModel):
    ConnectorId: StrictStr
