from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectRuleTriggerEventSource(BaseModel):
    EventSourceName: StrictStr | None = None
    IntegrationAssociationId: StrictStr | None = None
