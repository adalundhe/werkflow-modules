from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectFilters(BaseModel):
    Queues: list[StrictStr] | None = None
    Channels: list[Literal['VOICE', 'CHAT', 'TASK', 'EMAIL']] | None = None
    RoutingProfiles: list[StrictStr] | None = None
    RoutingStepExpressions: list[StrictStr] | None = None
    AgentStatuses: list[StrictStr] | None = None
    Subtypes: list[StrictStr] | None = None
    ValidationTestTypes: list[StrictStr] | None = None
