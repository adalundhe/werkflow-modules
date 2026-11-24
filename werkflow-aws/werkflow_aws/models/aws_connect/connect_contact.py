from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_additional_email_recipients import ConnectAdditionalEmailRecipients
from .connect_agent_info import ConnectAgentInfo
from .connect_campaign import ConnectCampaign
from .connect_case_entry import ConnectCaseEntry
from .connect_chat_metrics import ConnectChatMetrics
from .connect_contact_details import ConnectContactDetails
from .connect_contact_evaluation import ConnectContactEvaluation
from .connect_contact_lens import ConnectContactLens
from .connect_customer import ConnectCustomer
from .connect_customer_voice_activity import ConnectCustomerVoiceActivity
from .connect_disconnect_details import ConnectDisconnectDetails
from .connect_endpoint_info import ConnectEndpointInfo
from .connect_global_resiliency_metadata import ConnectGlobalResiliencyMetadata
from .connect_next_contact_entry import ConnectNextContactEntry
from .connect_outbound_strategy import ConnectOutboundStrategy
from .connect_quality_metrics import ConnectQualityMetrics
from .connect_queue_info import ConnectQueueInfo
from .connect_recording_info import ConnectRecordingInfo
from .connect_routing_criteria import ConnectRoutingCriteria
from .connect_segment_attribute_value import ConnectSegmentAttributeValue
from .connect_task_template_info_v2 import ConnectTaskTemplateInfoV2
from .connect_voicemail_info import ConnectVoicemailInfo
from .connect_wisdom_info import ConnectWisdomInfo


class ConnectContact(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    InitialContactId: StrictStr | None = None
    PreviousContactId: StrictStr | None = None
    ContactAssociationId: StrictStr | None = None
    InitiationMethod: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Channel: StrictStr | None = None
    QueueInfo: ConnectQueueInfo | None = None
    AgentInfo: ConnectAgentInfo | None = None
    InitiationTimestamp: datetime.datetime | StrictStr | None = None
    DisconnectTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    LastPausedTimestamp: datetime.datetime | StrictStr | None = None
    LastResumedTimestamp: datetime.datetime | StrictStr | None = None
    RingStartTimestamp: datetime.datetime | StrictStr | None = None
    TotalPauseCount: StrictInt | None = None
    TotalPauseDurationInSeconds: StrictInt | None = None
    ScheduledTimestamp: datetime.datetime | StrictStr | None = None
    RelatedContactId: StrictStr | None = None
    WisdomInfo: ConnectWisdomInfo | None = None
    CustomerId: StrictStr | None = None
    CustomerEndpoint: ConnectEndpointInfo | None = None
    SystemEndpoint: ConnectEndpointInfo | None = None
    QueueTimeAdjustmentSeconds: StrictInt | None = None
    QueuePriority: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ConnectedToSystemTimestamp: datetime.datetime | StrictStr | None = None
    RoutingCriteria: ConnectRoutingCriteria | None = None
    Customer: ConnectCustomer | None = None
    Campaign: ConnectCampaign | None = None
    AnsweringMachineDetectionStatus: StrictStr | None = None
    CustomerVoiceActivity: ConnectCustomerVoiceActivity | None = None
    QualityMetrics: ConnectQualityMetrics | None = None
    ChatMetrics: ConnectChatMetrics | None = None
    DisconnectDetails: ConnectDisconnectDetails | None = None
    AdditionalEmailRecipients: ConnectAdditionalEmailRecipients | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    Recordings: list[ConnectRecordingInfo] | None = None
    DisconnectReason: StrictStr | None = None
    ContactEvaluations: dict[StrictStr, ConnectContactEvaluation] | None = None
    TaskTemplateInfo: ConnectTaskTemplateInfoV2 | None = None
    Cases: list[ConnectCaseEntry] | None = None
    ContactDetails: ConnectContactDetails | None = None
    OutboundStrategy: ConnectOutboundStrategy | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    NextContacts: list[ConnectNextContactEntry] | None = None
    GlobalResiliencyMetadata: ConnectGlobalResiliencyMetadata | None = None
    ContactLens: ConnectContactLens | None = None
    VoicemailInfo: ConnectVoicemailInfo | None = None
