from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTTlsContext(BaseModel):
    serverName: StrictStr | None = None
