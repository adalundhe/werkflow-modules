from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_contact_filter import ConnectContactFilter


class ConnectUserDataFilters(BaseModel):
    Queues: list[StrictStr] | None = None
    ContactFilter: ConnectContactFilter | None = None
    RoutingProfiles: list[StrictStr] | None = None
    Agents: list[StrictStr] | None = None
    UserHierarchyGroups: list[StrictStr] | None = None
