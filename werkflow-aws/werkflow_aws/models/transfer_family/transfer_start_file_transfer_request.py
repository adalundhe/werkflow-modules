from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_custom_http_header import TransferCustomHttpHeader


class TransferStartFileTransferRequest(BaseModel):
    ConnectorId: StrictStr
    SendFilePaths: list[StrictStr] | None = None
    RetrieveFilePaths: list[StrictStr] | None = None
    LocalDirectoryPath: StrictStr | None = None
    RemoteDirectoryPath: StrictStr | None = None
    CustomHttpHeaders: list[TransferCustomHttpHeader] | None = None
