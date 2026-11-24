from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectPersistentConnectionConfig(BaseModel):
    Channel: StrictStr | None = None
    PersistentConnection: StrictBool | None = None
