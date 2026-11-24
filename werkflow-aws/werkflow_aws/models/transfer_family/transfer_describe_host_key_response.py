from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_host_key import TransferDescribedHostKey


class TransferDescribeHostKeyResponse(BaseModel):
    HostKey: TransferDescribedHostKey | None = None
    ResponseMetadata: dict[str, Any] | None = None
