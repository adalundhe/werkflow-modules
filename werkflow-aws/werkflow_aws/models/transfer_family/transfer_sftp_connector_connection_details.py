from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferSftpConnectorConnectionDetails(BaseModel):
    HostKey: StrictStr | None = None
