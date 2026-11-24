from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowRedshiftConnectorProfileCredentials(BaseModel):
    username: StrictStr | None = None
    password: StrictStr | None = None
