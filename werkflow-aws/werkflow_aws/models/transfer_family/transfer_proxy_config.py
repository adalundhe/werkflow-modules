from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferProxyConfig(BaseModel):
    SftpMode: StrictStr | None = None
