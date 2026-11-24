from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_agent_hierarchy_groups import ConnectAgentHierarchyGroups
from .connect_ai_agents_criteria import ConnectAiAgentsCriteria
from .connect_contact_analysis import ConnectContactAnalysis
from .connect_control_plane_tag_filter import ConnectControlPlaneTagFilter
from .connect_name_criteria import ConnectNameCriteria
from .connect_search_contacts_additional_time_range import ConnectSearchContactsAdditionalTimeRange
from .connect_searchable_contact_attributes import ConnectSearchableContactAttributes
from .connect_searchable_routing_criteria import ConnectSearchableRoutingCriteria
from .connect_searchable_segment_attributes import ConnectSearchableSegmentAttributes


class ConnectSearchCriteria(BaseModel):
    Name: ConnectNameCriteria | None = None
    AgentIds: list[StrictStr] | None = None
    AgentHierarchyGroups: ConnectAgentHierarchyGroups | None = None
    Channels: list[Literal['VOICE', 'CHAT', 'TASK', 'EMAIL']] | None = None
    ContactAnalysis: ConnectContactAnalysis | None = None
    InitiationMethods: list[Literal['INBOUND', 'OUTBOUND', 'TRANSFER', 'QUEUE_TRANSFER', 'CALLBACK', 'API', 'DISCONNECT', 'MONITOR', 'EXTERNAL_OUTBOUND', 'WEBRTC_API', 'AGENT_REPLY', 'FLOW']] | None = None
    QueueIds: list[StrictStr] | None = None
    RoutingCriteria: ConnectSearchableRoutingCriteria | None = None
    AdditionalTimeRange: ConnectSearchContactsAdditionalTimeRange | None = None
    SearchableContactAttributes: ConnectSearchableContactAttributes | None = None
    SearchableSegmentAttributes: ConnectSearchableSegmentAttributes | None = None
    ActiveRegions: list[StrictStr] | None = None
    ContactTags: ConnectControlPlaneTagFilter | None = None
    AiAgents: ConnectAiAgentsCriteria | None = None
