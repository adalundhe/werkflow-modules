from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_device_info import ConnectDeviceInfo
from .connect_hierarchy_groups import ConnectHierarchyGroups
from .connect_participant_capabilities import ConnectParticipantCapabilities
from .connect_state_transition import ConnectStateTransition


class ConnectAgentInfo(BaseModel):
    Id: StrictStr | None = None
    AcceptedByAgentTimestamp: datetime.datetime | StrictStr | None = None
    PreviewEndTimestamp: datetime.datetime | StrictStr | None = None
    ConnectedToAgentTimestamp: datetime.datetime | StrictStr | None = None
    AgentPauseDurationInSeconds: StrictInt | None = None
    HierarchyGroups: ConnectHierarchyGroups | None = None
    DeviceInfo: ConnectDeviceInfo | None = None
    Capabilities: ConnectParticipantCapabilities | None = None
    AfterContactWorkDuration: StrictInt | None = None
    AfterContactWorkStartTimestamp: datetime.datetime | StrictStr | None = None
    AfterContactWorkEndTimestamp: datetime.datetime | StrictStr | None = None
    AgentInitiatedHoldDuration: StrictInt | None = None
    StateTransitions: list[ConnectStateTransition] | None = None
    VoiceEnhancementMode: StrictStr | None = None
    ActiveRegion: StrictStr | None = None
