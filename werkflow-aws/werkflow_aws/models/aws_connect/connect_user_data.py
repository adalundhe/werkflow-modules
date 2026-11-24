from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_agent_contact_reference import ConnectAgentContactReference
from .connect_agent_status_reference import ConnectAgentStatusReference
from .connect_hierarchy_path_reference import ConnectHierarchyPathReference
from .connect_routing_profile_reference import ConnectRoutingProfileReference
from .connect_user_reference import ConnectUserReference


class ConnectUserData(BaseModel):
    User: ConnectUserReference | None = None
    RoutingProfile: ConnectRoutingProfileReference | None = None
    HierarchyPath: ConnectHierarchyPathReference | None = None
    Status: ConnectAgentStatusReference | None = None
    AvailableSlotsByChannel: dict[StrictStr, StrictInt] | None = None
    MaxSlotsByChannel: dict[StrictStr, StrictInt] | None = None
    ActiveSlotsByChannel: dict[StrictStr, StrictInt] | None = None
    Contacts: list[ConnectAgentContactReference] | None = None
    NextStatus: StrictStr | None = None
