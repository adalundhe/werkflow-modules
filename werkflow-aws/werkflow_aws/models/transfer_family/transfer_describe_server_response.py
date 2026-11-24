from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_server import TransferDescribedServer


class TransferDescribeServerResponse(BaseModel):
    Server: TransferDescribedServer | None = None
    ResponseMetadata: dict[str, Any] | None = None
