from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeAppSyncParameters(BaseModel):
    GraphQLOperation: StrictStr | None = None
