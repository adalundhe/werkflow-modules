from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_number_preference_item import EndUserMessagingNumberPreferenceItem
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingRequestPhoneNumberRequest(BaseModel):
    IsoCountryCode: StrictStr
    MessageType: Literal['TRANSACTIONAL', 'PROMOTIONAL']
    NumberCapabilities: list[Literal['SMS', 'VOICE', 'MMS', 'RCS']]
    NumberType: Literal['LONG_CODE', 'TOLL_FREE', 'TEN_DLC', 'SIMULATOR']
    OptOutListName: StrictStr | None = None
    PoolId: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    NumberPreference: list[EndUserMessagingNumberPreferenceItem] | None = None
    InternationalSendingEnabled: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ClientToken: StrictStr | None = None
