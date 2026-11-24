from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_host_key import TransferListedHostKey


class TransferListHostKeysResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServerId: StrictStr | None = None
    HostKeys: list[TransferListedHostKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
