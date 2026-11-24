from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EndUserMessagingSendTextMessageRequest(BaseModel):
    DestinationPhoneNumber: StrictStr
    OriginationIdentity: StrictStr | None = None
    MessageBody: StrictStr | None = None
    MessageType: Literal['TRANSACTIONAL', 'PROMOTIONAL'] | None = None
    Keyword: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    MaxPrice: StrictStr | None = None
    TimeToLive: StrictInt | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    DestinationCountryParameters: dict[Literal['IN_TEMPLATE_ID', 'IN_ENTITY_ID'], StrictStr] | None = None
    DryRun: StrictBool | None = None
    ProtectConfigurationId: StrictStr | None = None
    MessageFeedbackEnabled: StrictBool | None = None
