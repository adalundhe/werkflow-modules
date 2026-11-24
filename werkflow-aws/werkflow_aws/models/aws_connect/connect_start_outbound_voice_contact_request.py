from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_answer_machine_detection_config import ConnectAnswerMachineDetectionConfig
from .connect_outbound_strategy import ConnectOutboundStrategy
from .connect_reference import ConnectReference


class ConnectStartOutboundVoiceContactRequest(BaseModel):
    DestinationPhoneNumber: StrictStr
    ContactFlowId: StrictStr
    InstanceId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    References: dict[StrictStr, ConnectReference] | None = None
    RelatedContactId: StrictStr | None = None
    ClientToken: StrictStr | None = None
    SourcePhoneNumber: StrictStr | None = None
    QueueId: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    AnswerMachineDetectionConfig: ConnectAnswerMachineDetectionConfig | None = None
    CampaignId: StrictStr | None = None
    TrafficType: Literal['GENERAL', 'CAMPAIGN'] | None = None
    OutboundStrategy: ConnectOutboundStrategy | None = None
    RingTimeoutInSeconds: StrictInt | None = None
