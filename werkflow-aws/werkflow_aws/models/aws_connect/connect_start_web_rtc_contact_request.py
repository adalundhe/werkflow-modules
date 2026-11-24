from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_allowed_capabilities import ConnectAllowedCapabilities
from .connect_participant_details import ConnectParticipantDetails
from .connect_reference import ConnectReference
from .connect_segment_attribute_value import ConnectSegmentAttributeValue


class ConnectStartWebRTCContactRequest(BaseModel):
    ContactFlowId: StrictStr
    InstanceId: StrictStr
    ParticipantDetails: ConnectParticipantDetails
    Attributes: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
    AllowedCapabilities: ConnectAllowedCapabilities | None = None
    RelatedContactId: StrictStr | None = None
    References: dict[StrictStr, ConnectReference] | None = None
    Description: StrictStr | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
