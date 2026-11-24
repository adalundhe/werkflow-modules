from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferSftpPortWithOptions(BaseModel):
    SftpPort: StrictInt | None = None
    CommunicationMode: StrictStr | None = None
