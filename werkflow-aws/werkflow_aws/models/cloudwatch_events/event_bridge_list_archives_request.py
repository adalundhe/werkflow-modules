from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListArchivesRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    EventSourceArn: StrictStr | None = None
    State: Literal['ENABLED', 'DISABLED', 'CREATING', 'UPDATING', 'CREATE_FAILED', 'UPDATE_FAILED'] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
