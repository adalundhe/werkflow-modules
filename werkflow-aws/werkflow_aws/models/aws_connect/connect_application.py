from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectApplication(BaseModel):
    Namespace: StrictStr | None = None
    ApplicationPermissions: list[StrictStr] | None = None
    Type: StrictStr | None = None
