from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_virtual_interface_test_history import DirectConnectVirtualInterfaceTestHistory


class DirectConnectListVirtualInterfaceTestHistoryResponse(BaseModel):
    virtualInterfaceTestHistory: list[DirectConnectVirtualInterfaceTestHistory] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
