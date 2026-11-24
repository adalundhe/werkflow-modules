from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerContextStore(BaseModel):
    GlobalNetworkId: StrictStr | None = None
    ContextStoreId: StrictStr | None = None
    ContextStoreArn: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
