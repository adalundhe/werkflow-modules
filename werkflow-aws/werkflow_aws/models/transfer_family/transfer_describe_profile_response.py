from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_profile import TransferDescribedProfile


class TransferDescribeProfileResponse(BaseModel):
    Profile: TransferDescribedProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
