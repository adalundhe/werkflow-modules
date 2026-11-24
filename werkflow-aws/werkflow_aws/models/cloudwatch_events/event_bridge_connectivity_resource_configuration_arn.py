from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeConnectivityResourceConfigurationArn(BaseModel):
    ResourceConfigurationArn: StrictStr
