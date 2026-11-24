from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_queue_reference import ConnectQueueReference


class ConnectAgentContactReference(BaseModel):
    ContactId: StrictStr | None = None
    Channel: StrictStr | None = None
    InitiationMethod: StrictStr | None = None
    AgentContactState: StrictStr | None = None
    StateStartTimestamp: datetime.datetime | StrictStr | None = None
    ConnectedToAgentTimestamp: datetime.datetime | StrictStr | None = None
    Queue: ConnectQueueReference | None = None
