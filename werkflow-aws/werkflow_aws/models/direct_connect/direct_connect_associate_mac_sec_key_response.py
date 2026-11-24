from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_mac_sec_key import DirectConnectMacSecKey


class DirectConnectAssociateMacSecKeyResponse(BaseModel):
    connectionId: StrictStr | None = None
    macSecKeys: list[DirectConnectMacSecKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
