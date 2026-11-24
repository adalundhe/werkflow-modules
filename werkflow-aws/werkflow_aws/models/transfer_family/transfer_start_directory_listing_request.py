from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferStartDirectoryListingRequest(BaseModel):
    ConnectorId: StrictStr
    RemoteDirectoryPath: StrictStr
    OutputDirectoryPath: StrictStr
    MaxItems: StrictInt | None = None
