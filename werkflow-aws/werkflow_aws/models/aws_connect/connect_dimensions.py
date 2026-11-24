from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_agent_status_identifier import ConnectAgentStatusIdentifier
from .connect_queue_reference import ConnectQueueReference
from .connect_routing_profile_reference import ConnectRoutingProfileReference


class ConnectDimensions(BaseModel):
    Queue: ConnectQueueReference | None = None
    Channel: StrictStr | None = None
    RoutingProfile: ConnectRoutingProfileReference | None = None
    RoutingStepExpression: StrictStr | None = None
    AgentStatus: ConnectAgentStatusIdentifier | None = None
    Subtype: StrictStr | None = None
    ValidationTestType: StrictStr | None = None
