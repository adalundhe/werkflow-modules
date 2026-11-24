from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEventBridgeActionDefinition(BaseModel):
    Name: StrictStr | None = None
