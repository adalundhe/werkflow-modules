from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowInforNexusConnectorProfileCredentials(BaseModel):
    accessKeyId: StrictStr
    userId: StrictStr
    secretAccessKey: StrictStr
    datakey: StrictStr
