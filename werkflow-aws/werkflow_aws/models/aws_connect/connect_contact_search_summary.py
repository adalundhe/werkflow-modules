from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_contact_search_summary_agent_info import ConnectContactSearchSummaryAgentInfo
from .connect_contact_search_summary_ai_agent_info import ConnectContactSearchSummaryAiAgentInfo
from .connect_contact_search_summary_queue_info import ConnectContactSearchSummaryQueueInfo
from .connect_contact_search_summary_segment_attribute_value import ConnectContactSearchSummarySegmentAttributeValue
from .connect_global_resiliency_metadata import ConnectGlobalResiliencyMetadata
from .connect_routing_criteria import ConnectRoutingCriteria


class ConnectContactSearchSummary(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    InitialContactId: StrictStr | None = None
    PreviousContactId: StrictStr | None = None
    InitiationMethod: StrictStr | None = None
    Channel: StrictStr | None = None
    QueueInfo: ConnectContactSearchSummaryQueueInfo | None = None
    AgentInfo: ConnectContactSearchSummaryAgentInfo | None = None
    InitiationTimestamp: datetime.datetime | StrictStr | None = None
    DisconnectTimestamp: datetime.datetime | StrictStr | None = None
    ScheduledTimestamp: datetime.datetime | StrictStr | None = None
    SegmentAttributes: dict[StrictStr, ConnectContactSearchSummarySegmentAttributeValue] | None = None
    Name: StrictStr | None = None
    RoutingCriteria: ConnectRoutingCriteria | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    GlobalResiliencyMetadata: ConnectGlobalResiliencyMetadata | None = None
    AiAgentInfo: list[ConnectContactSearchSummaryAiAgentInfo] | None = None
