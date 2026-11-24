from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_described_access import TransferDescribedAccess


class TransferDescribeAccessResponse(BaseModel):
    ServerId: StrictStr | None = None
    Access: TransferDescribedAccess | None = None
    ResponseMetadata: dict[str, Any] | None = None
