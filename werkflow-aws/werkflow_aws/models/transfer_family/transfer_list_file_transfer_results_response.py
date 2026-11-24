from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_connector_file_transfer_result import TransferConnectorFileTransferResult


class TransferListFileTransferResultsResponse(BaseModel):
    FileTransferResults: list[TransferConnectorFileTransferResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
