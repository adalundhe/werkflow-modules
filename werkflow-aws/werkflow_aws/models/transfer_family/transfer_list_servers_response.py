from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_server import TransferListedServer


class TransferListServersResponse(BaseModel):
    NextToken: StrictStr | None = None
    Servers: list[TransferListedServer] | None = None
    ResponseMetadata: dict[str, Any] | None = None
