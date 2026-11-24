from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListConnectionsRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    ConnectionState: Literal['CREATING', 'UPDATING', 'DELETING', 'AUTHORIZED', 'DEAUTHORIZED', 'AUTHORIZING', 'DEAUTHORIZING', 'ACTIVE', 'FAILED_CONNECTIVITY'] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
