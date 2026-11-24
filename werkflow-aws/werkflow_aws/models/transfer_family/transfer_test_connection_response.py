from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_sftp_connector_connection_details import TransferSftpConnectorConnectionDetails


class TransferTestConnectionResponse(BaseModel):
    ConnectorId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    SftpConnectionDetails: TransferSftpConnectorConnectionDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
