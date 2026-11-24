from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_access import TransferListedAccess


class TransferListAccessesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServerId: StrictStr | None = None
    Accesses: list[TransferListedAccess] | None = None
    ResponseMetadata: dict[str, Any] | None = None
