from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_ai_agent import ConnectAIAgent
from .connect_application import ConnectApplication
from .connect_flow_module import ConnectFlowModule
from .connect_granular_access_control_configuration import ConnectGranularAccessControlConfiguration


class ConnectUpdateSecurityProfileRequest(BaseModel):
    SecurityProfileId: StrictStr
    InstanceId: StrictStr
    Description: StrictStr | None = None
    Permissions: list[StrictStr] | None = None
    AllowedAccessControlTags: dict[StrictStr, StrictStr] | None = None
    TagRestrictedResources: list[StrictStr] | None = None
    Applications: list[ConnectApplication] | None = None
    HierarchyRestrictedResources: list[StrictStr] | None = None
    AllowedAccessControlHierarchyGroupId: StrictStr | None = None
    AllowedFlowModules: list[ConnectFlowModule] | None = None
    AllowedAIAgents: list[ConnectAIAgent] | None = None
    GranularAccessControlConfiguration: ConnectGranularAccessControlConfiguration | None = None
