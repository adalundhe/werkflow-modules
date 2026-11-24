from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerConnectAttachmentOptions(BaseModel):
    Protocol: StrictStr | None = None
