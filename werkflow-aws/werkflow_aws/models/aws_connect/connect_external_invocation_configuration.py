from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ConnectExternalInvocationConfiguration(BaseModel):
    Enabled: StrictBool | None = None
