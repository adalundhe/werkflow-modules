from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_described_user import TransferDescribedUser


class TransferDescribeUserResponse(BaseModel):
    ServerId: StrictStr | None = None
    User: TransferDescribedUser | None = None
    ResponseMetadata: dict[str, Any] | None = None
