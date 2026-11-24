from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_connector import TransferDescribedConnector


class TransferDescribeConnectorResponse(BaseModel):
    Connector: TransferDescribedConnector | None = None
    ResponseMetadata: dict[str, Any] | None = None
