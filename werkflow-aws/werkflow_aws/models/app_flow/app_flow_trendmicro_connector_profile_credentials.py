from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowTrendmicroConnectorProfileCredentials(BaseModel):
    apiSecretKey: StrictStr
