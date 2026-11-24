from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_connector import TransferListedConnector


class TransferListConnectorsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Connectors: list[TransferListedConnector] | None = None
    ResponseMetadata: dict[str, Any] | None = None
